__author__ = 'jhala'



import re
import numpy
import json
import logging
logger = logging.getLogger('SerializeImageFeatures.py')
import Helpers


def ToDict(lcImageDataFile):
    logger.info('Serializng Land cover data in '+ lcImageDataFile + ' to dictionary')

    try:
        eDict=Helpers.getLandCoverReferenceDict()
        print eDict

        lineNo=0
        elemNameArr=[]
        elemDataArr=[]
        elemNamePosition=0

        for i in open(lcImageDataFile,'r'):
            lineNo+=1
            line=i.strip()
            logger.info(line)


            if lineNo==1 and re.match("^[0-9,]*$", line):
                elemNameArr = line.split(',')

            if lineNo==2 and re.match("^[0-9,.]*$",i):
                elemDataArr = line.split(',')

            if lineNo > 2:
                break

        if lineNo <2:
            logger.error('I expected at least 2 lines of data in land cover. File format has been changed. System Will break')

        for i in elemNameArr:

            keyName = 'L1_'+ str(i)
            logger.info(keyName)
            try:
                val =  str(elemDataArr[elemNamePosition])
            except IndexError:
                logger.exception('No data found matching key:'+ keyName + ' in landcover output')
                raise
            except:
                logger.exception('Other error reading landcover data')
                raise

            try:
                eDict["data"][keyName] = elemDataArr[elemNamePosition]
            except KeyError:
                logger.exception( 'Invalid Data in landcover output.'+ keyName + '. Tried to find this key in ' + str(eDict))
            except:
                logger.exception( 'Other error while assigning land cover data to dictionary' + str(eDict))
                raise


            elemNamePosition +=1

        # lets check the dictionary to make sure it does not have all 0's

        #valSet= set([ v for k,v in eDict.iteritems()])
        #if len(valSet) == 1 and '0' in valSet:
        #    logger.error('No Land Cover Data was extracted for this image. Something must be wrong.')


        return eDict



    except:
        logger.exception('Error Getting Land cover data from matlab land cover file: '+ lcImageDataFile)
        raise