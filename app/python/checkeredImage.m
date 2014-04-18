function [  ] = checkeredImage(I2,LCT2,R)
	RGB2 = ind2rgb(LCT2,lccmap) * 255;
	[M,N,PP] = size(I2);
	block_size = 75;
	P = ceil(M / block_size);
	Q = ceil(N / block_size);
	alpha_data = checkerboard(block_size, P, Q) > 0;
	alpha_data = alpha_data(1:M, 1:N);
	alpha_data = repmat(alpha_data,[1 1 3]);
	I3 = I2;
	I3(alpha_data==0) = RGB2(alpha_data==0);
	imshow(I3);
end;