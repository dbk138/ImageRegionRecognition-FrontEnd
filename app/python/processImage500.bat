@echo off
set SCRIPT_HOME=D:\SWENG_500_GRP_1\SWENG_500\_Matlab
set PATH=%PATH%;%SCRIPT_HOME%
REM echo p1 %1 
REM echo p2 %2 
REM echo p3 %3 
REM echo p4 %4
d:
cd %SCRIPT_HOME%
REM matlab -wait -nodesktop -nosplash -r  "ProcessImage(\"'%1'\",\"'%2'\",\"'%3'\",\"'%4'\",'FALSE')"
matlab -wait -nodesktop -nosplash -r  "try,diary('%5');ProcessImage(\"'%1'\",\"'%2'\",\"'%3'\",\"'%4'\",'FALSE');diary off;end,quit"
exit %ERRORLEVEL%