# QGIS-log-datasources
Python script to log all the datasources QGIS during a session are opening and using.

This script logs each and every datasource QGIS is opening and report this event to a common csv file (normally placed on a common networked drive). The purpose is to find which datasources that *actually* are used and perhaps deprecate / remove maintained but *unused* datasources in your organization.

Every time QGIS starts, it will execute the startup.py script. The script activates an event function, that registers every time QGIS opens a new layer and report this event into a csv file.

## Installation
The startup.py python script has to be copied every computer with QGIS installed and placed in the QGIS application directory for each user on the computer: "%appdata%\QGIS\QGIS3" (alongside the "profiles" directory)

![Udklip](https://user-images.githubusercontent.com/1866520/187031406-7b210161-bf60-4e3b-84d3-e262d0162653.jpg)

## Installation using the "install.cmd" Windows command script
If you place the *startup.py* and the *install.cmd* files together in an abitrary directory you can install the startup.py by double-clicking on the *install.cmd* from Windows File Explorer. The install script checks if there is an existing startup.py and renames this to startup.deprecated_<*timestamp*>.py before installing the new startup.py. 

## Setup
Is is possible to change several types of settings by changing constant values inside the script. All settings are documented in the script using comments.



