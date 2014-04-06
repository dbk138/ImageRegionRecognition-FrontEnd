function [  ] = semanticElements(lcImage )
       LCT1 = imread(lcImage)
	   %%numberOfDimensions = ndims(LCT1)
	   I = rgb2gray(LCT1)
	   disp(numberOfDimensions)
      [counts,pixelvalue]=imhist(I);
                    percs = counts(counts()>0);
                    vals = pixelvalue(counts()>0);
                    percs = percs/sum(percs);
					disp(vals)
					disp(percs)

end
					