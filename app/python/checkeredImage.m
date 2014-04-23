function [  ] = checkeredImage(I2,LCT2,R)
    [landCoverImage,lccmap] = imread(LCT2);
	[Image,imageMap] = imread(I2);
	%%whos LCT2
	info = imfinfo(LCT2)
    %%whos lccmap
	%%RGB2 = ind2rgb(landCoverImage,lccmap)   * 255;
	%% info shows that LCT2 is already an RGB image so we do not need the rgb command.
	[M,N,PP] = size(Image);
	block_size = 75;
	P = ceil(M / block_size);
	Q = ceil(N / block_size);
	alpha_data = checkerboard(block_size, P, Q) > 0;
	alpha_data = alpha_data(1:M, 1:N);
	alpha_data = repmat(alpha_data,[1 1 3]);
	I3 = Image;
	I3(alpha_data==0) = landCoverImage(alpha_data==0);
	%%imshow(I3);
	imwrite(I3,'checkeredImage.jpg')
end