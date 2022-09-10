@echo of

set app_dir=%appdata%\QGIS\QGIS3
set inst_dir=%~dp0
set tstmp=%date:~6,4%_%date:~3,2%_%date:~0,2%_%time:~0,2%_%time:~3,2%_%time:~6,2%
if exist "%app_dir%\startup.py" move "%app_dir%\startup.py" "%app_dir%\startup.deprecated_%tstmp%.py" 
copy "%inst_dir%startup.py" "%app_dir%\startup.py"
