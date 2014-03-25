__author__ = 'jhala'
#from bottle import route, run, debug, template, request,  static_file, error, response
from bottle import default_app, route, run,response

@route('/getlocations', method='GET')
def new_item():
    import ImageList
    response.content_type = 'application/json'
    return ImageList.getImageList()

