__author__ = 'jhala'

import unittest
import Helpers
import os

class UnitTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_mainImageListIsPopulated(self):
        self.assertGreater(len(Helpers.getMainImageFileList()),1)

    def test_mainImageListIsList(self):
        self.assertEquals(type(Helpers.getMainImageFileList()),list)

    def test_imageLocation(self):
        self.assertTrue(os.path.isdir(Helpers.getImageLocation()))

    def test_landCoverRefDataIsDict(self):
        self.assertTrue(type(Helpers.getLandCoverReferenceDict()),dict)

    def test_imageDataLocation(self):
        self.assertTrue(os.path.isdir(Helpers.getImageDataLocation()))

    def test_matLabProcessImageScript(self):
        self.assertTrue(os.path.isfile(Helpers.getMatLabProcessImageScript()))

    def test_imageOutputLoc(self):
        self.assertTrue(os.path.isdir(Helpers.getImageOutputLoc()))

    def test_matLabSemanticElementsScript(self):
        self.assertTrue(os.path.isfile(Helpers.getMatLabSemanticElementsScript()))

    def test_isMainImageFile(self):
        fileName = 'anImage.jpg'
        self.assertTrue(Helpers.isMainImageFile(fileName))

    def test_isNotMainImageFile(self):
        fileName = 'anImageLC.jpg'
        self.assertFalse(Helpers.isMainImageFile(fileName))

    # def test_getLCImageName(self):
    #     fileName = 'anImage.jpg'
    #     self.assertEquals(Helpers.getLCImageName(fileName),'anImageLC.jpg')






#if __name__ == '__main__':
#    unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
unittest.TextTestRunner(verbosity=5).run(suite)