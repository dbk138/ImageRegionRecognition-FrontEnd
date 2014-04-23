function [  ] = semanticElements(lcImage )
    [LCT] = imread(lcImage);
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
    csvwrite('landcover.csv',landcover);