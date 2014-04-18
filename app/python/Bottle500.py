__author__ = 'jhala'
#from bottle import route, run, debug, template, request,  static_file, error, response
from bottle import route,response, request
import json

@route('/getlocations', method='GET')
def new_item():
    import ImageList
    response.content_type = 'application/json'
    return ImageList.getImageList()

@route('/syslog', method='GET')
def new_item():
    logList=[]
    response.content_type = 'application/json'
    for i in open('sys.log','r'):
        logList.append(i)
    logList.reverse()
    return json.dumps(logList)

@route('/query', method='POST')
def query():
    import ProcessImage
    response.content_type = 'application/json'
    q = json.load(request.body)

    queryString = q['queryString']
    imageName= q['imgName']
    lcImageName= q['lcImageName']
    directory = q['directory']

    ProcessImage.process_image(imageName, lcImageName, queryString, directory)

    return { 'Your query' : queryString }



