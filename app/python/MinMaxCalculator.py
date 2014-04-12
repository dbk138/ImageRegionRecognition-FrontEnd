
import logging
import logging.config
import sys
import os
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(os.path.basename(sys.argv[0]))
import Helpers


def rMinMax():
    import SysCall
    for i in [ 'min','max']:
        err,out,retCode=SysCall.sh(['rscript',Helpers.getR_MinMaxScript(),'allImagesDataDump.txt',i,'min1.csv','>','NUL'])

def getAllDataPoints():
    import json
    nl='\r\n'
    Helpers.removeAllImagesDataDumpFile()
    df=open(Helpers.getAllImagesDataDumpFile(),'w')
    df.write('key,val'+nl)
    for i in Helpers.getMainDataFileList():
        imageData=json.load(open(i))
        for k,v in imageData['data'].iteritems():
            df.write(k+','+v+nl)

df.close()

print err,out



