__author__ = 'jhala'

import re
import os
import json

def getImageList():
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