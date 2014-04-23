__author__ = 'jhala'


import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('ImageDataWriter')
import Helpers
import SysCall
import SerializeSemanticElements
import json
matLabFeatureScr=Helpers.getMatLabFeatureExtractScript()
matLabSemanticElementsScr=Helpers.getMatLabSemanticElementsScript()
import MinMaxCalculator


def semanticElements(lcImageName):

    try:
        Helpers.removeMatlabSemanticElementsOutputFile()
        Helpers.removeMatlabSemanticElementsCsvFile()
        #logger.info('Running '+ matLabSemanticElementsScr)
        out,err,retCd = SysCall.sh([matLabSemanticElementsScr, '"'+ lcImageName +'"'])

        if Helpers.checkFileNameExists(Helpers.getSemanticElementsCsvFile()):
            return SerializeSemanticElements.ToDict(Helpers.getSemanticElementsCsvFile())
        else:
            logger.error('Semantic Summary Not Created. This is a major error. Has something changed in the system that would make the matlab call unstable? File name expected is '+ Helpers.getSemanticElementsCsvFile() )
            return {}

    except:
        logger.exception('Error Updating Features For '+lcImageName)
        raise

if __name__ == '__main__':
    counter=0
    logger.info('Run Start')

    for i in Helpers.getMainImageFileList():

        try:
            if i['dataFileRequiresUpdate']:
                logger.info('Image Requires Update: '+i['imageFile'])
                if i['lcImageExists']:
                    semanticElementsDict=semanticElements(i['lcImageName'])
                    if Helpers.fileNotInFlux(i['lcImageName']) or Helpers.fileNotInFlux(i['imageFile']):

                        if len(semanticElementsDict) > 0:
                            imgDict={}
                            imgDict['data'] = {}

                            for k,v in semanticElementsDict['data'].iteritems():
                                imgDict['data'][k] = v

                            logger.info('Writing data to ' + i['dataFile'])
                            f = open(i['dataFile'],'w')
                            f.write(json.dumps(imgDict))
                            f.close()

                            counter+=1
                        else:
                            logger.error('Something went terribly wrong while  getting data from matlab, Image Features or Semantic elements are null')
                    else:
                        logger.warn('Skip processing this file because it appears to be in the state of being copied.')
                else:
                    logger.error('Nothing will be done because LC file is missing:' + i['lcImageName'])
        except:
            logger.exception('Exceptions getting info from image and lc files' + i['lcImageName'] + 'and ' + i['imageFile'])

    logger.info('Run End. Images Processed: '+str(counter))










