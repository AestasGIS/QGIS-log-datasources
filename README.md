# QGIS-log-datasources
Python script to log all the datasources QGIS are using.

This script logs each and every datasource QGIS is opening and report this event to a common csv file. The purpose is find which datasources that actually are used and perhaps
deprecate / remove maintained but unused datasources.

Every time QGIS starts, it will execute the script. The script installs a event function, that registers every time QGIS opens a new layer and report this event into a csv file.

## Installation
The startup.py python script has to be copied every computer with QGIS installed and placed in the QGIS application directory for each user on the computer: "%appdata%\QGIS\QGIS3" (besides the "profiles" directory)

![Udklip](https://user-images.githubusercontent.com/1866520/187031406-7b210161-bf60-4e3b-84d3-e262d0162653.jpg)

## Setup
Is is possible to change several types of settings by changing constant values inside the script. All settings are documentet using comments



