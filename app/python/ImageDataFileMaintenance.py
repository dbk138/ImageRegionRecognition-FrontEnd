
import logging
import logging.config
import sys
import os
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(os.path.basename(sys.argv[0]))

import Helpers

def DeleteObsoleteDataFiles():

    mainDataFileList= Helpers.getMainDataFileList()

    allDataFiles=Helpers.getAllDataFilesList()

    for i in allDataFiles:
        try:
            logger.info( 'Found: '+ str(mainDataFileList.index(i)))
        except ValueError:
            logger.info( i +  'Does not have a corresponding image file.')
            Helpers.deleteDataFile(i)

if __name__ == '__main__':
    logger.info('Cleaning up data files whose corresponding image files have been deleted.')
    logger.setLevel(logging.WARNING)
    DeleteObsoleteDataFiles()

