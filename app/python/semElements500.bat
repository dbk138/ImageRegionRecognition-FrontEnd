echo off
set SCRIPT_HOME=D:\SWENG_500_GRP_1\SWENG_500\_Matlab
set PATH=%PATH%;%SCRIPT_HOME%
REM echo Your image %1
d:
cd %SCRIPT_HOME%
REM matlab -wait -nodesktop -nosplash /r FeaturesForImage('%1','FALSE')
matlab -wait -nodesktop -nosplash -r "try,diary('semElements.out.txt'); semanticElements(\"'%1'\"); diary off; end, quit"
REM , quit