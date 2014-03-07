__author__ = 'jhala'
from decimal import Decimal

import json
import Helpers

''' Creates a lookup of features. The min/max values represent the min max for the entire set per feature '''

''' main '''
if __name__ == "__main__":
    fil=r"c:\capstone\featureInfo.csv"
    outFil = r"c:\capstone\featureLookup.json"

    fileArr=Helpers.fileInfo(fil)
    header=Helpers.getHeader(fileArr)
    featureDict={}

    for column in header[1:]:   #skipping the image name (first - column)

        columnData=[]
        #for data in fileArr[1:]: # skipping the header row (first - row)
        for data in fileArr[1:]: # skipping the header row (first - row)
            columnData.append(Decimal(data[header.index(column)]))
        columnData.sort()
        featureDict[column] = { "minval": str(columnData[0]) ,  "maxval" : str(columnData[len(columnData)-1]) }

    of = open(outFil,'w')
    json.dump(featureDict,of,indent=4, separators=(',', ': '))
    of.close()





