__author__ = 'jhala'

import os
import json
import Helpers
def getImageList():
<<<<<<< HEAD

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

    return json.dumps(mainImageList)
=======
    imgList=[]
    cnt=0
    for root, dirs, files in os.walk(r'C:\Users\geoimages\angular-seed\app\images'):

        cnt+=1
        if cnt==1:
            continue


        #print root
        locName=os.path.basename(root)
        #print locName
        thisImageInfo={}
        thisImage={}
        thisImageList=[]
        thisImageInfo['name']= locName

        for i in files:
            imgName=os.path.join(root,i)
            if re.search('.jpg$',imgName, flags=re.IGNORECASE) and not re.search('LC.jpg$',imgName, flags=re.IGNORECASE):
                thisImage['name'] = locName + '/' + os.path.basename(imgName)
                thisImageList.append(thisImage)
                print thisImage
        thisImageInfo['images'] = thisImageList
        imgList.append(thisImageInfo)


    return json.dumps(imgList)

    #print imgList
    #print thisImage
    #f = open('dict.json','w')
    #json.dump(imgList,f,indent=4, separators=(',', ': '))
    #f.close()
>>>>>>> 0426b42c0aada7e2745a3ec11224b8b2dd460d32
