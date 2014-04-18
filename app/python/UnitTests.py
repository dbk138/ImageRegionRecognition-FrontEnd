__author__ = 'jhala'

import unittest
from Helpers import getMainImageFileList

class UnitTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_mainImageListIsPopulated(self):
        self.assertGreater(len(getMainImageFileList()),1)

    def test_mainImageListIsList(self):
        self.assertEquals(type(getMainImageFileList()),list)


if __name__ == '__main__':
    unittest.main()
