__author__ = 'jhala'

import Helpers
import json
import os

''' creates a location lookup, and an associated image lookup '''

''' main '''
if __name__ == "__main__":
    fil = r"c:\capstone\featureInfo.csv"
    outLoc = r"c:\capstone\locationLookup.json"
    imageBaseDir="C:\\Users\\jhala\\angular-seed\\app\\images\\"

    fileArr = Helpers.fileInfo(fil)
    headerArr = Helpers.getHeader(fileArr)

    locationsDict = {}
    locations=[]
    locationsFinal=[]
    locationId = 0
    rowId = 0
    existingLoc={}
    for row in fileArr[1:]:
        colCounter = 0
        thisImageCount=0
        imagesForThisLocation=[]
        imagesForThisLocationTmp=[]
        for col in row:
            if headerArr[colCounter] == 'imgName':
                imgName = col.replace("E:/GeoImages/", "")

                locationArr = imgName.split("/")
                locationName = locationArr[0]

                if not os.path.exists(imageBaseDir + locationName ):
                    break

                if len(locationArr[0:len(locationArr) - 1]) > 1:
                    print "Nested loc alert"

                print locationArr[0]
                try:
                    locIndex=locations.index(locationName)
                    imagesForThisLocationTmp = locationsFinal[locIndex]['images']
                    imagesForThisLocationTmp.append( { 'name' : imgName})
                    locationsFinal[locIndex] = { 'name' :  locationsFinal[locIndex]['name'] , 'id' : locationsFinal[locIndex]['id'] , 'numImages' : locationsFinal[locIndex]['numImages']+1 , 'images' : imagesForThisLocationTmp }

                except ValueError:
                    locationId += 1
                    locations.append(locationName)
                    thisImageCount  += 1
                    imagesForThisLocation = { 'name': imgName}
                    locationsFinal.append({ 'name' : locationName , 'id' : locationId, 'numImages' : thisImageCount, 'images': [ imagesForThisLocation ]})
                break

            colCounter += 1
        rowId += 1


    ol = open(outLoc,'w')
    json.dump(locationsFinal,ol,indent=4, separators=(',', ': '))
    ol.close()


