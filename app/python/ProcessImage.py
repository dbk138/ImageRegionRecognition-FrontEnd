import Helpers
import SysCall
import logging

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('ProcessImage.py')



def process_image(imageName, lcImageName, queryString, directory):
    try:
        matLabProcessImageScr=Helpers.getMatLabProcessImageScript()
        logger.info('Running '+ matLabProcessImageScr + ' for: ' + imageName+' '+ queryString+' '+lcImageName+' '+directory)
        out,err,retCd = SysCall.sh([matLabProcessImageScr, '"'+imageName+'"', '"'+lcImageName+'"', queryString, '"'+directory+'"', 'false'])

        logger.info(out)
        logger.info(err)
        logger.info(retCd)
        logger.info('End ')

        return  {"ProcesImage": "Success" }
    except:
        logger.exception('Error Processing Image.')
        #raise