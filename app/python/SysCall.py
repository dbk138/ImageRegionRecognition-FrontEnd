
import subprocess as sub
import re
import sys
import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

def sh(cmdArray):
    try:
        return execute(cmdArray,True)
    except:
        logger.exception('Error running command: '+ ' '.join(cmdArray))

    return "error occurred with call:", sys.exc_info() , 1

def execute(array, shellTrueFalse):
    print 'exec ' + ' '.join(array)
    logger.info('Executing: '+' '.join(array) )
    if shellTrueFalse:
        p = sub.Popen(' '.join(array), stdout=sub.PIPE, stderr=sub.PIPE, shell=shellTrueFalse)
    else:
        p = sub.Popen(array, stdout=sub.PIPE, stderr=sub.PIPE, shell=shellTrueFalse)

    output,errors = p.communicate()

    strOutput=str(output)
    strErrors=str(errors)

    return strOutput,strErrors,p.returncode
