__author__ = 'jhala'
import types
import os.path, time
import json
import logging
import logging.config
#import sys
#logging.config.fileConfig('logging.conf')
import re
import hashlib
logger = logging.getLogger('Helpers.py')


appInfo='appinfo.json'

'''
Check that the file is not in the process of being copied
'''
def fileNotInFlux(fileName):
    h1=hashlib.md5(open(fileName).read()).hexdigest()
    time.sleep(.5)
    if h1 == hashlib.md5(open(fileName).read()).hexdigest():
        return True # file is same
    else:
        return False  # file is being copied


def logTest():
    logger.info('T E S T')

''' Helper Functions '''

'''  get the file as an array of arrays ( header + rows and columns) '''
def fileInfo(fil):
    fileArr=[]
    for i in open(fil):
        fileArr.append(i.strip().split(","))

    return fileArr

def deleteDataFile(fileName):
    # lets first check that the data file is actually where its supposed to be

    if getImageDataLocation() in fileName and '.json' in fileName and os.path.isfile(fileName):
        print logger.info('Removing obsolete datafile: '+ fileName)
        try:
            os.remove(fileName)
        except:
            logger.exception('Could not remove file:'+ fileName)
    else:
        logger.warn( "Are you crazy you want to delete a file that is not a data file: "+ fileName)

''' returns the list of data files corresponding to images '''
def getMainDataFileList():
    dataFileList=[]
    for i in getMainImageFileList():
        dataFileList.append( i['dataFile'])
    return dataFileList

''' get all data files, regardless of whether image file exists '''
def getAllDataFilesList():
    import glob
    return glob.glob(getImageDataLocation() + r'\*.json')

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

def getLandCoverReferenceFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['LandCoverReference']

def getLandCoverReferenceDict():
    f=open(getLandCoverReferenceFile(),'r')
    return json.load(f)



def getFeatureLookupFileName():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['FeatureLookupDataFile']

def isBatchSystemEnabled():
    f=open(appInfo,'r')
    loc=json.load(f)
    tf=str(loc['BatchSystemEnabledFile'])
    if tf.lower() == 'true':
        return True
    else:
        return False

def getR_MinMaxScript():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['R_min_max_script']

def getAllImagesDataDumpFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['AllImagesDataDumpFile']

def getAllImagesMinDataDumpFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['AllImagesMinDataDumpFile']

def getAllImagesMaxDataDumpFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['AllImagesMaxDataDumpFile']

def removeAllImagesDataDumpFiles():
    logger.info('Removing all files involved in calculating min/max values across dataset.')
    fileName=getAllImagesDataDumpFile()
    minFileName=getAllImagesMinDataDumpFile()
    maxFileName=getAllImagesMaxDataDumpFile()
    if os.path.exists(fileName) and os.path.isfile(fileName):
        try:
            os.remove(fileName)
        except:
            logger.exception('Could Not Delete File' + fileName)

    if os.path.exists(minFileName) and os.path.isfile(minFileName):
        try:
            os.remove(minFileName)
        except:
            logger.exception('Could Not Delete File' + fileName)

    if os.path.exists(maxFileName) and os.path.isfile(maxFileName):
        try:
            os.remove(maxFileName)
        except:
            logger.exception('Could Not Delete File' + fileName)


def getImageDataLocation():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['imageData']



def getMatLabFeatureExtractScript():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabFeatureExtractScript']

def getMatLabProcessImageScript():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabProcessImageScript']

def getImageOutputLoc():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['imageOutput']

def getMatLabProcessImageOutputFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabProcessImageOutputFile']

def removeMatLabProcessImageOutputFile():
    f=getMatLabProcessImageOutputFile()
    if os.path.exists(f) and os.path.isfile(f):
        os.remove(f)

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

def getSemanticElementsCsvFile():
    f=open(appInfo,'r')
    loc=json.load(f)
    return loc['matlabSemanticElementsCsvFile']

def removeMatlabSemanticElementsCsvFile():
    f=getSemanticElementsCsvFile()
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
                    dataFileLastTouched=epoch  # if no json file set its date to epoch start.

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

