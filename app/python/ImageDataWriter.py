__author__ = 'jhala'


import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('ImageDataWriter')
import Helpers
import SysCall
import SerializeImageFeatures
import time
import SerializeSemanticElements
import json
matLabFeatureScr=Helpers.getMatLabFeatureExtractScript()
matLabSemanticElementsScr=Helpers.getMatLabSemanticElementsScript()
import MinMaxCalculator

def features(i):

    #logger.info('Image:' +i['imageFile'] + ' modified %s ' % time.ctime(i['imageLastTouched']))
    #logger.info('Image:' +i['dataFile'] + ' Exists: '+ str(i['dataFileExists']) + ' Modified %s ' % time.ctime(i['dataLastTouched']))
    #logger.info('Requires Update: '+str(i['dataFileRequiresUpdate']))

    try:
        Helpers.removeMatlabFeatureOutputFile()
        #logger.info('Running '+ matLabFeatureScr)
        out,err,retCd = SysCall.sh([matLabFeatureScr, '"'+i['imageFile']+'"', 'false'])

        if Helpers.checkFileNameExists(Helpers.getMatlabFeatureOutputFile()):
            return SerializeImageFeatures.ToDict(Helpers.getMatlabFeatureOutputFile())
        else:
            return {}

    except:
        logger.exception('Error Updating Features For '+i['imageFile'])
        raise

def semanticElements(i):

    try:
        Helpers.removeMatlabSemanticElementsOutputFile()
        #logger.info('Running '+ matLabSemanticElementsScr)
        out,err,retCd = SysCall.sh([matLabSemanticElementsScr, '"'+i['lcImageName']+'"'])

        if Helpers.checkFileNameExists(Helpers.getMatlabFeatureOutputFile()):
            return SerializeSemanticElements.ToDict(Helpers.getMatlabSemanticElementsOutputFile())
        else:
            return {}

    except:
        logger.exception('Error Updating Features For '+i['imageFile'])
        raise

if __name__ == '__main__':
    counter=0
    logger.info('Run Start')
    #print Helpers.getMainImageFileList()
    for i in Helpers.getMainImageFileList():

        try:
            if i['dataFileRequiresUpdate']:
                logger.info('Image Requires Update: '+i['imageFile'])
                if i['lcImageExists']:
                    imgFeaturesDict=features(i)
                    semanticElementsDict=semanticElements(i)

                    if len(imgFeaturesDict) > 0 and len(semanticElementsDict) > 0:
                        imgDict={}
                        imgDict['data'] = {}

                        for k,v in imgFeaturesDict['data'].iteritems():
                            imgDict['data'][k] = v

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
                    logger.error('Nothing will be done because LC file is missing:' + i['lcImageName'])
        except:
            logger.exception('Exceptions getting info from image and lc files' + i['lcImageName'] + 'and ' + i['imageFile'])

    logger.info('Run End. Images Processed: '+str(counter))

    if counter > 0:
        MinMaxCalculator.Calculate()









