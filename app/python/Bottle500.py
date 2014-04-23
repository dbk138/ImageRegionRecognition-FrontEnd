__author__ = 'jhala'
#from bottle import route, run, debug, template, request,  static_file, error, response
from bottle import route, response, request
import json
import os


@route('/getlocations', method='GET')
def new_item():
    import ImageList

    response.content_type = 'application/json'
    return ImageList.getImageList()


@route('/syslog', method='GET')
def syslog():
    logList = []
    response.content_type = 'application/json'
    try:
        for i in open('sys.log', 'r'):
            logList.append(i)
        logList.reverse()
    except:
        logList.append('Sys.log not found in app directory')
    
    return json.dumps(logList)

@route('/querylog', method='GET')
def querylog():
    logList = []
    response.content_type = 'application/json'
    try:
        for i in open('query.log', 'r'):
            logList.append(i)
        logList.reverse()
    except:
        logList.append('Query.log file not found in app directory.')

    return json.dumps(logList)

@route('/unittestlog', method='GET')
def unittestlog():
    logList = []
    response.content_type = 'application/json'
    try:
        for i in open('unittest.log', 'r'):
            logList.append(i)
    except:
        logList.append('Unittest.Log file not found in app directory.')

    return json.dumps(logList)



@route('/query', method='POST')
def query():
    import ProcessImage

    response.content_type = 'application/json'
    q = json.load(request.body)

    queryString = str(q['queryString'])
    queryString = queryString.replace(" ","").replace("\t","").strip()
    imageName = str(q['imgName'])
    lcImageName = str(q['lcImageName'])
    dir = q['dir']

    ProcessImage.process_image(imageName, lcImageName, queryString, dir)

    return {'Your query': queryString}



