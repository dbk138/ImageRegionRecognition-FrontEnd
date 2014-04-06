__author__ = 'jhala'



import re
import numpy
import json


def ToDict(lcImageDataFile):
    dataStart=False
    pixelVals=[]

    semElements = [ 'L1_100','L1_110','L1_150','L1_160','L1_200','L1_210','L1_240', 'L1_250', 'L1_255' ]
    binArr = [ 0, 100, 110, 150, 160, 200, 210, 240, 250, 255 ]

    for i in open(lcImageDataFile,'r'):
        line = i.strip()

        if  re.match("^I =$", line):
            dataStart = True
            continue

        if dataStart:
            valsOnThisLine= line.split(" ")
            for pixelVal in valsOnThisLine:
                if re.match("[0-9]", pixelVal):
                    pixelVals.append(int(pixelVal))

    pixelVals.sort()

    hist, edges = numpy.histogram( pixelVals , bins = binArr)
    totalPixels= len(pixelVals)
    imgDict={}
    imgDict['data'] = {}
    counter=0

    for h1 in hist:
        x= float(h1)/float(totalPixels)
        imgDict['data'][semElements[counter]] = str(x)
        counter +=1
    return imgDict