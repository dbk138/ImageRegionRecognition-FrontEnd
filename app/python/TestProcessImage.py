__author__ = 'geoimages'

import sys

import ProcessImage
import Helpers

if __name__ == '__main__':


    testimage= r'C:\Users\geoimages\angular-seed\app\images\Alvin NE\Alvin NE_w012_h014.jpg'
    testLCimage= r'C:\Users\geoimages\angular-seed\app\images\Alvin NE\Alvin NE_w012_h014LC.jpg'
    directory = Helpers.getImageOutputLoc()
    ProcessImage.process_image(testimage, testLCimage, 'Area_35_500#Perimeter_50_300')