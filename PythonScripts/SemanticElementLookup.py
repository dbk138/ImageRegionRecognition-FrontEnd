__author__ = 'jhala'

import re
import json

''' creates a dictionary of semantic elements '''


if __name__ == "__main__":
    fil=r"c:\capstone\SemanticElements.csv"
    outFil = r"c:\capstone\SemanticElements.json"

    elementDict={}
    subElementDict={}
    prevMainId=None
    mainId=None
    lineNo=0
    for row in open(fil):
        lineNo=lineNo+1

        m = re.match( r"\(([0-9]*)\)", row)  # this is a main element
        if m:
            #print "Row: ",lineNo , row.strip()
            rowArr=row.strip().split(" ")

            # keep a track of the previous main id.
            if mainId <> None:
                prevMainId = mainId
            mainId= m.group(1)
            if prevMainId <> mainId and prevMainId <> None:
                #this main feature group has been processed so lets add the subelements.
                elementDict[prevMainId]["SubElements"] = subElementDict
                subElementDict = {}  # and reset the subElement Dict

            #print 'new element', mainId, rowArr[2], 'prev element', prevMainId
            try:
                elementDict[mainId]
            except KeyError:
                elementDict[mainId]={}
                elementDict[mainId]["Description"] = rowArr[2]

        n = re.match(r"^-([0-9]*)",row)
        if n:
            rowArr=row.strip().split(",")
            subElementDict[n.group(1)]=re.sub(r"\.","",re.sub(r"[0-9]","","".join(rowArr[1:]))).lstrip().rstrip()

    elementDict[mainId]["SubElements"] = subElementDict  # add the last set of sub elements to the dict.



    of = open(outFil,'w')
    json.dump(elementDict,of,indent=4, separators=(',', ': '))
    of.close()
