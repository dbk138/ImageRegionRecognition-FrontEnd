__author__ = 'jhala'


import re
import sys
import logging
import logging.config
import Helpers
import SysCall
import MatlabOutputToJson
import time
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('BatchFeatureExtract')

matLabFeatureScr=Helpers.getMatLabFeatureExtractScript()
updateCount=0
errorCount=0

limit=0
logger.info('Run Start:' +time.strftime("%m-%d-%Y %H:%M:%S"))
for i in Helpers.getMainImageFileList():
    #print i
    #break
    #logger.info('Image:' +i['imageFile'] + ' modified %s ' % time.ctime(i['imageLastTouched']))
    #logger.info('Image:' +i['dataFile'] + ' Exists: '+ str(i['dataFileExists']) + ' Modified %s ' % time.ctime(i['dataLastTouched']))
    #logger.info('Requires Update: '+str(i['dataFileRequiresUpdate']))
    if i['dataFileRequiresUpdate']:
        logger.info('Image:' +i['imageFile'] + ' modified %s ' % time.ctime(i['imageLastTouched']))
        logger.info('Image:' +i['dataFile'] + ' Exists: '+ str(i['dataFileExists']) + ' Modified %s ' % time.ctime(i['dataLastTouched']))
        logger.info('Requires Update: '+str(i['dataFileRequiresUpdate']))
        limit+=1
        if limit > 1:
            1
            break
        logger.info('Needs Update: '+i['imageFile'])
        try:
            Helpers.removeMatlabFeatureOutputFile()
            logger.info('Running '+ matLabFeatureScr)
            out,err,retCd = SysCall.sh([matLabFeatureScr, '"'+i['imageFile']+'"', 'false'])
            #out,err,retCd = SysCall.sh([matLabFeatureScr, Helpers.getTestImageName(), 'false'])
            logger.info('ret code:' +str(retCd))
            logger.info('Script returned: ' + str( out))
            if retCd <> 0:
                logger.error('Script Returned Error'+ err)
                logger.error('Stdout from script' + out)
                continue

            jsonString=MatlabOutputToJson.Get(Helpers.getMatlabFeatureOutputFile())
            logger.info('Writing data to ' + i['dataFile'])
            f = open(i['dataFile'],'w')
            f.write(jsonString)
            f.close()

            updateCount+=1

        except:
            logger.exception('Error Updating Features For '+i['imageFile'])
            errorCount+=1

logger.info('Feature Update Ran # of images: ' + str(updateCount))

if errorCount > 0:
    logger.error('Feature Update Errored out for # of images: ' + str(errorCount))

logger.info('Run End:' +time.strftime("%m-%d-%Y %H:%M:%S"))




