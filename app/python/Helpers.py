__author__ = 'jhala'
import types
import os.path, time
import json
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

''' Helper Functions '''

'''  get the file as an array of arrays ( header + rows and columns) '''
def fileInfo(fil):
    fileArr=[]
    for i in open(fil):
        fileArr.append(i.strip().split(","))

    return fileArr


''' Return the header as an array '''
def getHeader(fileArr):
    for rowOne in fileArr:
        return rowOne


def fileLastTouchedTime(fileName):
    mtim= int(os.path.getmtime(fileName))
    ctim= int(os.path.getctime(fileName))
    tims = [ mtim, ctim]
    tims.sort()
    return tims[len(tims)-1]


def getImageLocation():
    f=open('appinfo.json','r')
    loc=json.load(f)
    return loc['imageLocation']

def getImageDataLocation():
    f=open('appinfo.json','r')
    loc=json.load(f)
    return loc['imageData']

def getMatLabFeatureExtractScript():
    f=open('appinfo.json','r')
    loc=json.load(f)
    return loc['matlabFeatureExtractScript']

def getMatlabFeatureOutputFile():
    f=open('appinfo.json','r')
    loc=json.load(f)
    return loc['matlabFeatureOutputFile']


def getTestImageName():
    f=open('appinfo.json','r')
    loc=json.load(f)
    return loc['testImage']

def removeMatlabFeatureOutputFile():
    f=getMatlabFeatureOutputFile()
    if os.path.exists(f) and os.path.isfile(f):
        os.remove(f)

def checkFileNameExists(filName=str):
    return os.path.exists(filName) and os.path.isfile(filName)

def getMainImageFileList():
    fileList=[]
    epoch=time.mktime(time.strptime('1970','%Y'))
    for root, dirs, files in os.walk(getImageLocation()):
        #print root
        #print dirs
        for fil in files:
            thisFileName=os.path.join(root, fil)
            dataFileExists=False
            imageFileNewerThanDataFile=False
            dataFileRequiresUpdate=False
            if isMainImageFile(thisFileName) and checkFileNameExists(thisFileName):

                mainImageLastTouched=fileLastTouchedTime(thisFileName)
                expectedDataFileName = os.path.join(getImageDataLocation(), os.path.basename(root)+'_'+fil+'.json')
                if checkFileNameExists(expectedDataFileName ):
                    dataFileExists=True
                    dataFileLastTouched=fileLastTouchedTime(expectedDataFileName)
                else:
                    dataFileExists=False
                    dataFileLastTouched=epoch

                if dataFileExists and ( mainImageLastTouched > dataFileLastTouched) :
                    dataFileRequiresUpdate=True

                if not dataFileExists:
                    dataFileRequiresUpdate=True


                fileList.append({ 'dataFileRequiresUpdate' : dataFileRequiresUpdate, 'imageFile' : str(thisFileName), 'dataFile' : expectedDataFileName, 'imageLastTouched': mainImageLastTouched, 'dataLastTouched': dataFileLastTouched, 'dataFileExists' : dataFileExists} )

    return fileList


def isMainImageFile(fileName):
    import re
    if re.search('.jpg$',fileName, flags=re.IGNORECASE) and not re.search('LC.jpg$',fileName, flags=re.IGNORECASE):
        return True
    else:
        return False