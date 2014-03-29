__author__ = 'jhala'
import re
import Helpers
import logging
import logging.config
import json

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def Get(matlabFeatureOutputFile):
    isData=False
    imgDict = {}
    featureName=''
    stat=0
    for line in open(matlabFeatureOutputFile):
        lineStr=line.strip().replace(" ","").replace("'","")

        if re.search("^.*:.*$",lineStr) :   #if its after and not an empty line.
            #print lineStr
            lineArr=lineStr.split(":")

            if lineArr[0]=='imgName':
                featureName='imgName'
                stat=lineArr[1:]
            else:
                featureName=lineArr[0]
                stat=lineArr[1]

                if stat == "NaN":
                    stat = 0

            #print featureName,stat
            if featureName == 'imgName':
                try:
                    imgDict['imgName']
                except KeyError:
                    imgDict['imgName']= stat
            else:
                try:
                    imgDict['data']
                except KeyError:
                    imgDict['data'] = {}


                imgDict['data'][featureName] = float(stat)

                1 #imgDict["data"][featureName] = float(stat)




    #l='4.840458391220713e-01'
    #print float(l)

    return json.dumps(imgDict)


