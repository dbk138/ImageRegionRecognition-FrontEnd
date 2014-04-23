function [ featureValues ] = ProcessImage( imageName , landcoverImageName, pQueryString, directory, DEBUG )
% queryString should have a form
% 'property_min_max&property_min_max&...'like this:
% Area_0_35&Perimeter_0_50 where property is one of the elements of props1
% Directory should be in the form C:/Temp/

%% read images
% imagenName='test.jpg';
% landcoverImageName='testLC.jpg';
% read image
    queryString = strrep(pQueryString,'#','&')
	disp(queryString)
    imagen = imread(imageName);
	imagen = correctLighting(double(imagen), 'rgb');
% read landcover
    [LCT] = imread(landcoverImageName);
%% extract land cover percentage by pixel value
    LCTgray = rgb2gray(LCT);
% abstract landcover
    LCTgray( LCTgray < 105 ) = 100;                  % urban
    LCTgray( LCTgray < 149 & LCTgray >= 105 ) = 110; % agriculture
    LCTgray( LCTgray < 155 & LCTgray >= 149 ) = 150; % grassland
    LCTgray( LCTgray < 195 & LCTgray >= 155 ) = 160; % forest
    LCTgray( LCTgray < 205 & LCTgray >= 195 ) = 200; % water
    LCTgray( LCTgray < 235 & LCTgray >= 205 ) = 210; % wetland
    LCTgray( LCTgray < 245 & LCTgray >= 235 ) = 240; % barren
    LCTgray( LCTgray < 252 & LCTgray >= 245 ) = 250; % shrubland
    LCTgray( LCTgray < 300 & LCTgray >= 252 ) = 255; % Cloudy
    
    [counts,pixelvalue]=imhist( LCTgray );
% keep only cover above 1 percent
    counts(counts()<0.01*sum(counts)) = 0;
    percs = counts(counts()>0);
    vals = pixelvalue(counts()>0);
    percs = percs/sum(percs);
% save landcover
    landcover = [transpose(vals);transpose(percs)];
    csvwrite(strcat(directory,'landcover.csv'),landcover);
%   landcover = csvread('c:/temp/landcover.csv'); % you can read it back
    
    clear landcover percs vals counts LCTgray pixelvalue;
    
%% prepare checkered image and save it
    [M,N,PP] = size(imagen);
    block_size = 40;
    P = ceil(M / block_size);
    Q = ceil(N / block_size);
    alpha_data = checkerboard(block_size, P, Q) > 0;
    alpha_data = alpha_data(1:M, 1:N);
    alpha_data = repmat(alpha_data,[1 1 3]);
    checkeredImage = imagen;
    checkeredImage(alpha_data==0) = LCT(alpha_data==0);
% imshow(checkeredImage);
% write the image
    imwrite(checkeredImage ,strcat(directory,'checkeredImage.jpg'),'jpg');

    clear M N PP block_size P Q alpha_data checkeredImage;

%% tokenize query input
% queryString = 'Area_35_500&Perimeter_50_300';
    predicates = strsplit(queryString,'&');
    query = [];
    for d=1:length(predicates)
        query = [query;strsplit(predicates{d},'_')];
    end
    query = transpose(query);
    
    clear predicates d;

%% set feature value vector
    featureValues = struct('imgName',imageName);
    
    if size(imagen,3)==3 % RGB image
        C = double(imagen(:,:,1));
        C = C(:);
        C = C(C>min(C));
        C = C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_R');
        
        C = double(imagen(:,:,2));
        C = C(:);
        C=C(C>min(C));
        C=C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_G');

        C = double(imagen(:,:,3));
        C = C(:);
        C=C(C>min(C));
        C=C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_B');
        
        I = rgb2hsv(double(imagen));
        C = double(I(:,:,1));
        C = C(:);
        C=C(C>min(C));
        C=C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_H');
        
        C = double(I(:,:,2));
        C = C(:);
        C=C(C>min(C));
        C=C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_S');

        C = double(I(:,:,3));
        C = C(:);
        C=C(C>min(C));
        C=C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_V');

        imagen=rgb2gray(imagen);
        
        clear C I;
    else
        C = double(imagen);
        C = C(:);
        C = C(C>min(C));
        C = C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_R');
        featureValues = basicFeatures(C,featureValues,'color_G');
        featureValues = basicFeatures(C,featureValues,'color_B');
        
        I = rgb2hsv(double(imagen));
        C = double(I(:,:,1));
        C = C(:);
        C=C(C>min(C));
        C=C(C<max(C));
        featureValues = basicFeatures(C,featureValues,'color_H');
        featureValues = basicFeatures(C,featureValues,'color_S');
        featureValues = basicFeatures(C,featureValues,'color_V');

        clear C I;
    end

	featureValues.('color_entropy') = entropy(double(imagen));

    distances = [1 4 9];
	for d=1:length(distances)
        offsets = [0 distances(d); -distances(d) distances(d); -distances(d) 0; -distances(d) -distances(d)];
        GLCMs = graycomatrix(imagen,'Offset',offsets);
        stats = graycoprops(GLCMs,{'Contrast',...
                                   'Correlation',...
                                   'Energy',...
                                   'Homogeneity'});
  
        featureValues.( ['color_contrast_' num2str(distances(d))]   ) = mean(stats.Contrast);
        featureValues.( ['color_correlation_' num2str(distances(d))]) = mean(stats.Correlation);
        featureValues.( ['color_energy_' num2str(distances(d))]     ) = mean(stats.Energy);
        featureValues.( ['color_homogeneity_' num2str(distances(d))]) = mean(stats.Homogeneity);
    end
    
    C = double(imagen);
    C = C(:);
    C=C(C>min(C));
    C=C(C<max(C));
    featureValues = basicFeatures(C,featureValues,'color_gray');
    clear C;

    imagen=imadjust(imagen,stretchlim(imagen),[0 1]);
    
%% Show image
%    if DEBUG
%        figure(1)
%        imshow(imagen);
%        title('INPUT IMAGE WITH NOISE')
%    end
%% Convert to binary image
    imagent = imagen;
    imagent(imagent == min(imagent(:))) = mean(imagen(:));
    imagent(imagent == max(imagent(:))) = mean(imagen(:));

    threshold = graythresh(imagent);
    imagent =~im2bw(imagen,threshold);
%% Remove all object containing fewer than 30 pixels
    imagent = bwareaopen(imagent,50);
    
    clear threshold;
%% fill a gap in the pen's cap
    se = strel('disk',2);
    imagent = imclose(imagent,se);
    imagent = imfill(imagent,'holes');

    clear se;
%% Show image binary image
%    if DEBUG
%        figure(2)
%        imshow(~imagent);
%        title('INPUT IMAGE WITHOUT NOISE')
%    end
%% Label connected components
    [L1,num1]=bwlabel(imagent);
%% Label inverse connected components
    imagent2 = imcomplement(imagent);
    [L2,num2]=bwlabel(imagent2);
%% construct overall regions    
    L = L1;
    L(L2 > 0) = L2(L2 > 0) + max(L1(:));                    
%% Save number of features    
	featureValues.( 'LIGHT_FEAT_NUM' )    = num1;
	featureValues.( 'DARK_FEAT_NUM' )     = num2;
	featureValues.( 'FEAT_NUM' )          = num1 + num2;

%% Measure properties of image regions
    props1 = {'Area','Centroid','EulerNumber','BoundingBox', ...
              'Extent','Perimeter','Orientation',...
              'ConvexArea','FilledArea','Eccentricity','MajorAxisLength',...
            'Solidity','EquivDiameter','MinorAxisLength'};
    propied=regionprops(L,props1);
    propiedStruct = struct2cell(propied);

    retFields = fieldnames(propied);
% this will store the regions that qualify    
    regionsToReturn = ones( [1,num1 + num2] );
    for fi=1:length(retFields)
        featureValues = basicFeatures([propied.(retFields{fi})],featureValues,['obj_' retFields{fi}]);
        
% get regions for query
        foundMatch = sum(strcmp(retFields{fi}, query(1,:)));
        
        if foundMatch > 0
            myquery = query(:,strcmp(retFields{fi}, query(1,:)));
            minquery = str2double(myquery(2));
            maxquery = str2double(myquery(3));
            
            myvalues = cell2mat(propiedStruct(fi,:));
            regionsToReturn = min(regionsToReturn,myvalues>=minquery & myvalues<=maxquery);
        end
    end
    
    regionIndexes = find(regionsToReturn);

    clear props1 myquery minquery maxquery myvaluesfoundMatch
    
%% Measure properties of image regions
    props2 = {'WeightedCentroid'}; 
    propied=regionprops(L,imagent,props2);

    retFields = fieldnames(propied);
    for fi=1:length(retFields)
        featureValues = basicFeatures([propied.(retFields{fi})],featureValues,['obj_' retFields{fi}]);
    end

    clear imagent quantiles retFields props2 fe fi propied
%% texture feature extraction
% [2 0] - each pixel is compared to the pixel 2 rows down, 0 columns over
% [0 2] - each pixel is compared to the pixel 0 rows away, 2 columns over.
    [GLCM2] = graycomatrix(imagen,'Offset',[2 0;0 2]);
    stats2 = GLCM_Features1(GLCM2,0);

    retFields = fieldnames(stats2);
    for fi=1:length(retFields)
        featureValues.(['texture_' retFields{fi} '_1'])=stats2.(retFields{fi})(1);
        featureValues.(['texture_' retFields{fi} '_2'])=stats2.(retFields{fi})(2);
    end

    clear GLCM2 fi stats2 retFields
%% Computes edge and corner phase congruency in an image
    [M, m, or, ft, pc, EO, T] = phasecong3(imagen);
    C = reshape(M,[size(M,1)*size(M,2),1]);
    featureValues = basicFeatures(C,featureValues,'obj_phase_congruency_max_moment' );
    C = reshape(m,[size(m,1)*size(m,2),1]);
    featureValues = basicFeatures(C,featureValues,'obj_phase_congruency_min_moment' );
    C = reshape(or,[size(or,1)*size(or,2),1]);
    featureValues = basicFeatures(C,featureValues,'obj_phase_congruency_orientation' );
    C = reshape(ft,[size(ft,1)*size(ft,2),1]);
    featureValues = basicFeatures(C,featureValues,'obj_phase_congruency_ft' );

    featureValues.('phase_congruency_noise_thresh')=T;
    clear C EO M T fe ft m or pc ans;

%% display custom image
%    Lfiltered = (L<5)|(L>60);
    Lfiltered = ismember(L,regionIndexes);
    regionImages = im2double(imagen).* Lfiltered;
    regionImages(regionImages==0) = 1; %% make ignored features white
    imwrite(regionImages ,strcat(directory,'regionsImage.jpg'),'jpg');

%    figure(num1)
%    imshow(regionImages)    
%    title('Objects')
    
    clear Lfiltered regionImages;
    
    
    clear imagen GLCMs L L1 L2
end
%% done here
