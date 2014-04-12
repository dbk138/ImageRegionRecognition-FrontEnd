
import subprocess as sub
import re
import sys
import logging
import logging.config

logger = logging.getLogger('SysCall.py')

def sh(cmdArray):
    try:
        return execute(cmdArray,True)
    except:
        logger.exception('Error running command: '+ ' '.join(cmdArray))

    return "error occurred with call:", sys.exc_info() , 1

def execute(array, shellTrueFalse):
    logger.info('Executing: '+' '.join(array) )
    if shellTrueFalse:
        p = sub.Popen(' '.join(array), stdout=sub.PIPE, stderr=sub.PIPE, shell=shellTrueFalse)
    else:
        p = sub.Popen(array, stdout=sub.PIPE, stderr=sub.PIPE, shell=shellTrueFalse)

    output,errors = p.communicate()

    strOutput=str(output)
    strErrors=str(errors)

    if p.returncode <> 0:
        logger.warn('External program returned non 0 exit code')

    if strErrors <> '':
        logger.warn('stderr: '+strErrors)

    if strOutput.replace(' ','') <> '':
        logger.info('stdout: '+strOutput)

    return strOutput,strErrors,p.returncode
