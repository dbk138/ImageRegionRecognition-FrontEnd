__author__ = 'jhala'

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
