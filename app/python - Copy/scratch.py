import Helpers

# f = open('syscall.py','r')
# print Helpers.getImageLocation()
#
# Helpers.fileLastTouchedTime(f)

import ImageList
#
#print ImageList.getImageList()

#print Helpers.getMainImageFileList()

import re
x=r"c:\x\abc2323.jpg"

r=re.match("(.*)(.jpg)", x, flags=re.IGNORECASE)
print r.groups()
print r.group(1) + "LC"+  r.group(2)


a = {   'data' : {  'x' : 1   , 'y': 2} }
b = {   'data' : {  'a' : 1   , 'b': 2} }
d={}
c= a.copy()
c.update(b)

print len(d)

imgDict={}
imgDict['data'] = {}
imgDict['data']['x'] ='aaa'

print imgDict

#import SysCall
#SysCall.sh(['dir'])