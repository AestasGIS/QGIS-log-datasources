# QGIS-log-datasources
Python script to log all the datasources QGIS is opening and using during a session.

This script logs each and every datasource QGIS is opening and report this event to a common csv file (normally placed on a common networked drive). 

## Why ? (use case)
The purpose is to find which datasources that *actually* are used - and deprecate / remove maintained but *unused* datasources in your organization. 
It's not uncommon for some organisations to use several hundred external datarepositories and copy data from the repositories to a local netwoked drive or import them to a spatial enabled database. Setup and on-going maintenance of the import process can be minimized by removing unused datasources.  

## How ? 
Every time QGIS starts, it will execute the startup.py script. The script activates an event function, that registers every time QGIS opens a new layer and report this event into a csv file.

## Installation
The startup.py python script has to be copied to every computer with QGIS installed and placed in the QGIS application directory for each user on the computer: "%appdata%\QGIS\QGIS3" (alongside the "profiles" directory)

![Udklip](https://user-images.githubusercontent.com/1866520/187031406-7b210161-bf60-4e3b-84d3-e262d0162653.jpg)

## Installation using the "install.cmd" Windows command script
If you place the *startup.py* and the *install.cmd* files together in an arbitrary directory you can install the startup.py by double-clicking on the *install.cmd* from Windows File Explorer. The install script checks if there is an existing startup.py and renames this to startup.deprecated_<*timestamp*>.py before installing the new startup.py. 

## Setup
Is is possible to change several types of settings by changing constant values inside the script. All settings are **documented** in the startup.py **script** using comments.



