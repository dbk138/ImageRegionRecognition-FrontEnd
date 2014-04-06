__author__ = 'jhala'
import types
import os.path, time
import json
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)
import re

appInfo='appinfo.json'

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
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['imageLocation']

def getImageDataLocation():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['imageData']

def getMatLabFeatureExtractScript():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabFeatureExtractScript']

def getMatLabSemanticElementsScript():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabSemanticElementsScript']

def getMatlabSemanticElementsOutputFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabSemanticElementsOutputFile']

def removeMatlabSemanticElementsOutputFile():
    f=getMatlabSemanticElementsOutputFile()
    if os.path.exists(f) and os.path.isfile(f):
        os.remove(f)

def getMatlabFeatureOutputFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabFeatureOutputFile']


def getTestImageName():
    f=open(appInfo,'r')
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

                lcImageExists=False
                lcImageName = getLCImageName(thisFileName)
                if lcImageName != None:
                    lcImageExists=True

                fileList.append({ 'lcImageExists': lcImageExists , 'lcImageName' : lcImageName, 'dataFileRequiresUpdate' : dataFileRequiresUpdate, 'imageFile' : str(thisFileName), 'dataFile' : expectedDataFileName, 'imageLastTouched': mainImageLastTouched, 'dataLastTouched': dataFileLastTouched, 'dataFileExists' : dataFileExists} )

    return fileList


def isMainImageFile(fileName):
    if re.search('.jpg$',fileName, flags=re.IGNORECASE) and not re.search('LC.jpg$',fileName, flags=re.IGNORECASE):
        return True
    else:
        return False

def getLCImageName(imageFileName):
    r=re.match("(.*)(.jpg)", imageFileName, flags=re.IGNORECASE)
    if not r:
        logger.error("Invalid image file name given" + imageFileName)
        return None
    else:
         lcImageName = r.group(1) + "LC"+  r.group(2)
         if checkFileNameExists(lcImageName):
             return lcImageName
         else:
             logger.error('Image file does not exist: ' +lcImageName)
             return None

