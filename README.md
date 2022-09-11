# QGIS-log-datasources
Python script to log all the datasources QGIS is opening and using during a session.

This script logs each and every datasource QGIS is opening and report this event to a csv file (normally placed on a networked drive shared by all users). 
The script should work on QGIS ver 3+ in Windows environments. It is possible getting it to work in a Linux environment by altering the location of the startup.py script and the csv file location (a constant value defined in the script).

## Why ? (use case)
It's not uncommon for some organisations to use several hundred external data-repositories and copy data from them to a local networked drive or importing them to a spatial enabled database. Setup and on-going maintenance of the data import process can be minimized by removing unused datasources.  

The purpose of the script is to find which datasources that *actually* are used so it's possible to deprecate / remove presently maintained but *unused* datasources in your organization, thus minimizing the administrative burden. 

## How ? 
Every time QGIS starts, it will execute the startup.py script. The script activates an event function, that registers every time QGIS opens a new layer and report this event into a common, shared csv file. 
After a period the csv file will contain the name of every datasource that has been opened by QGIS users. The csv file can then be examined by Excel using the pivot function. 

## Installation
The startup.py python script has to be copied to every computer with QGIS installed and placed in the QGIS application directory for each user on the computer: "%appdata%\QGIS\QGIS3" (alongside the "profiles" directory). 

![Udklip](https://user-images.githubusercontent.com/1866520/187031406-7b210161-bf60-4e3b-84d3-e262d0162653.jpg)

The easiest method (for you) is to ask your IT-department to make an update to the QGIS installation. However, it it possible to it manually update an existing QGIS installtion.

## Installation using the "install.cmd" Windows command script
If you place the *startup.py* and the *install.cmd* files together in an arbitrary directory you can install the startup.py by double-clicking on the *install.cmd* from Windows File Explorer. The install.cmd script checks if there is an existing startup.py and renames this to startup.deprecated_<*timestamp*>.py before installing the new startup.py. 

## Setup
Is is possible to change several types of settings by changing constant values inside the script. All settings are clearly **documented** in the startup.py **script** using comments. You can edit the script file with a simple text editor like NotePad



