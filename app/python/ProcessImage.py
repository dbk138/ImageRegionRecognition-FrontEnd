import logging
import logging.config
logging.config.fileConfig('queryLogging.conf')
logger = logging.getLogger('ProcessImage')

import Helpers
import SysCall
import sys
import os



def process_image(imageName, lcImageName, queryString, dir):
    try:
        Helpers.removeMatLabProcessImageOutputFile()
        directory = Helpers.getImageOutputLoc() + dir

        if not os.path.exists(directory):
            os.makedirs(directory)

        matLabProcessImageScr=Helpers.getMatLabProcessImageScript()
        logger.info('Start Query')
        out,err,retCd = SysCall.sh([matLabProcessImageScr, '"'+imageName+'"', '"'+lcImageName+'"', queryString, '"'+directory+'"', 'false', os.path.basename(Helpers.getMatLabProcessImageOutputFile())])
        logger.info('End ')

        return  {"ProcesImage": "Success" }
    except:
        logger.exception('Error Processing Image.')
        #raise