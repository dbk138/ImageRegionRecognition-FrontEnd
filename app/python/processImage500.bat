echo off
set SCRIPT_HOME=D:\SWENG_500_GRP_1\SWENG_500\_Matlab
set PATH=%PATH%;%SCRIPT_HOME%
echo p1 %1 
echo p2 %2 
echo p3 %3 
echo p4 %4
d:
cd %SCRIPT_HOME%
REM matlab -wait -nodesktop -nosplash /r FeaturesForImage('%1','FALSE')
REM matlab -wait -nodesktop -nosplash -r "try,diary('processImage.out.txt'); ProcessImage(\"'C:\Users\geoimages\Desktop\GeoWisconsin\Alvin NE\Alvin NE_w001_h002.jpg'\", \"'C:\Users\geoimages\Desktop\GeoWisconsin\Alvin NE\Alvin NE_w001_h002LC.jpg'\", \"'Area_35_500&Perimeter_50_300'\", \"'c:\temp\x\'\",\"'FALSE'\"); diary off; end"
REM matlab -wait -nodesktop -nosplash -r "try,diary('processImage.out.txt'); ProcessImage(\"'%1'\", \"'%2'\", \"'%3'\", \"'%4'\",'FALSE'); diary off; end"
REM , quit
REM matlab -wait -nodesktop -nosplash -r "ProcessImage('C:\Users\geoimages\Desktop\GeoWisconsin\Alvin NE\Alvin NE_w001_h002.jpg','C:\Users\geoimages\Desktop\GeoWisconsin\Alvin NE\Alvin NE_w001_h002LC.jpg','Area_35_500&Perimeter_50_300','c:\temp\x\','FALSE')"
matlab -wait -nodesktop -nosplash -r "try,diary('processImage.out.txt');  ProcessImage(\"'%1'\",\"'%2'\",\"'%3'\",\"'%4'\",'FALSE'); diary off; end ,quit"
exit %ERRORLEVEL%