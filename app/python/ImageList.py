__author__ = 'jhala'

import os
import json
import Helpers

def getImageList():

    # first lets create a simple dictionary of locations and images
    simpleImageDict={}
    for i in Helpers.getMainImageFileList():
        locName=os.path.basename(os.path.dirname(i['imageFile']))
        imgName=locName + '/'+ os.path.basename(i['imageFile'])
        print locName, imgName

        try:
            simpleImageDict[locName]
            imgList= simpleImageDict[locName]
            imgList.append(imgName)
        except:
            imgList= [imgName ]
            simpleImageDict[locName] =  imgList

    # next we create json that fits with the existing format of image list
    # which is a bit convoluted but served its purpose at one time..
    mainImageList=[]
    for k,v in simpleImageDict.iteritems():
        #print k
        imagesArr=[]
        for images in v:
            imageDict={ 'name' : images }
            imagesArr.append(imageDict)

        #print imagesArr

        oneLocationDict={}
        oneLocationDict['images'] = imagesArr
        oneLocationDict['name'] = k

        mainImageList.append(oneLocationDict)

    #f=open('test.json','w')
    #json.dump(mainImageList,f)
	
	# sort image list by location name. commented out. this will be done in the front end.
    #mainImageList.sort(key=operator.itemgetter('name'))
    return json.dumps(mainImageList)
