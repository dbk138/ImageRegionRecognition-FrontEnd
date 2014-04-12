
import logging
import logging.config
import sys
import os
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(os.path.basename(sys.argv[0]))
import Helpers
import json

def rMinMax():
    import SysCall
    try:
        logger.info('Calling R script to retrieve Min Values across datasest')
        out,err,retCode=SysCall.sh(['rscript',Helpers.getR_MinMaxScript(),Helpers.getAllImagesDataDumpFile(),'min',Helpers.getAllImagesMinDataDumpFile(),'>','NUL'])
        if retCode <> 0:
            logger.error("R script returned error" + err)
    except:
        logger.exception("Could not run R script")
        raise

    try:
        logger.info('Calling R script to retrieve Max Values across datasest')
        out,err,retCode=SysCall.sh(['rscript',Helpers.getR_MinMaxScript(),Helpers.getAllImagesDataDumpFile(),'max',Helpers.getAllImagesMaxDataDumpFile(),'>','NUL'])
        if retCode <> 0:
            logger.error("R script returned error" + err)
    except:
        logger.exception("Could not run R script")
        raise

def getAllDataPoints():
    logger.info('Building a list of all feature data points in file' + Helpers.getAllImagesDataDumpFile())

    nl='\r\n'
    df=open(Helpers.getAllImagesDataDumpFile(),'w')
    df.write('key,val'+nl)
    for i in Helpers.getMainDataFileList():
        imageData=json.load(open(i))
        for k,v in imageData['data'].iteritems():
            df.write(k+','+v+nl)
    df.close()


if __name__ == '__main__':
    logger.info('Calculate the Min Max feature values across the entire data set.')
    Helpers.removeAllImagesDataDumpFiles()
    getAllDataPoints()
    rMinMax()

    minMaxDict={}

    logger.info('Building Dictionary..')

    for i in open(Helpers.getAllImagesMinDataDumpFile()):
        minKeyVal=i.strip().replace('"','').split(",")
        #print minKeyVal[0]
        if minKeyVal[0] <> '':
            key=minKeyVal[0]
            val=minKeyVal[1]

            thisDict={ "minval" : str(val) }
            minMaxDict[key]=thisDict


    for i in open(Helpers.getAllImagesMaxDataDumpFile()):
        maxKeyVal=i.strip().replace('"','').split(",")
        if maxKeyVal[0] <> '':
            key=maxKeyVal[0]
            val=maxKeyVal[1]
            try:
                valDict=minMaxDict[key]
                valDict['maxval'] = val
            except KeyError:
                logger.exception('Major error while calculating min/max values across dataset, key:' + key + ' not found in min dataset but was found in max dataset')
                raise



    fl=open(Helpers.getFeatureLookupFileName(),'w')
    json.dump(minMaxDict,fl)
    fl.close()

    logger.info('Recreated file '+ Helpers.getFeatureLookupFileName())






