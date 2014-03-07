__author__ = 'jhala'

import Helpers
import json
import os

''' creates a location lookup, and an associated image lookup '''

''' main '''
if __name__ == "__main__":
    fil = r"c:\capstone\featureInfo.csv"
    outLoc = r"c:\capstone\locationLookup.json"
    imageSourceDir="C:\\Users\\jhala\\angular-seed\\app\\images\\"
    imageInfoOutDir="C:\\Users\\jhala\\angular-seed\\app\\data\\images\\"

    fileArr = Helpers.fileInfo(fil)
    headerArr = Helpers.getHeader(fileArr)
    imageList=[]
    rowId=0

    for row in fileArr[1:]:
        rowId +=1
        #if rowId == 2:
        #    break
        colCounter = 0
        imageDict={}
        #print 'items in row' + str(len(row))
        for col in row:
            # get the image name and location
            if headerArr[colCounter] == 'imgName':
                imgName = col.replace("E:/GeoImages/", "")
                locationArr = imgName.split("/")
                imgBaseName = locationArr[1]
                locationName = locationArr[0]
                imageDataFile=imageInfoOutDir + locationName + '_' + imgBaseName + '.json'

            # if the image dir given by barb does not exist then break
            if not os.path.exists(imageSourceDir + locationName ):
                break
            else:
                # write the data to the folder
                if headerArr[colCounter] == 'imgName':
                    f = open (imageDataFile,'w')

                if colCounter > 0:
                    #print headerArr[colCounter], col

                    try:
                        imageDict['data'][headerArr[colCounter]] = col
                    except KeyError:
                        imageDict['data'] = {}
                        imageDict['data'][headerArr[colCounter]] = col


                if colCounter + 1 ==len(row):
                    print 'reached end of image data'

                    json.dump(imageDict,f,indent=4, separators=(',', ': '))
                    f.close()
                    print 'wrote: ',imageDataFile

            colCounter += 1





        #rowId = rowId + 1




#    ol = open(outLoc,'w')
#    json.dump(locationsFinal,ol,indent=4, separators=(',', ': '))
#    ol.close()


