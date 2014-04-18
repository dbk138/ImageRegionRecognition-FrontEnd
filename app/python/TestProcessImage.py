__author__ = 'geoimages'

if __name__ == '__main__':
    import ProcessImage

    testimage= r'C:\Users\geoimages\angular-seed\app\images\Alvin NE\Alvin NE_w001_h001.jpg'
    testLCimage= r'C:\Users\geoimages\angular-seed\app\images\Alvin NE\Alvin NE_w001_h001LC.jpg'
    #directory = 'C:\\Users\\geoimages\\angular-seed\\app\\images\\Alvin NE\\'
    directory = 'C:\\temp\\\\'
    ProcessImage.process_image(testimage, testLCimage, 'Area_35_500#Perimeter_50_300',directory)