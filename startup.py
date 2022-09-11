from qgis.core import QgsProject, QgsMessageLog, Qgis, QgsRasterDataProvider
from datetime import datetime
from os import getlogin
from os.path import exists
from socket import gethostname

# Location of log file - Must be a network file and every QGIS user has to have write-access to this file
LOG_FILE = 'd:/tmp/loglag.csv'

# What to log (see examples on how to format row string)..
# You can use the following tokens: now : timestamp, host : hostname for computer, login : login name for user, 
#                                   name : layer name, uri : uri string for layer, stype : sourcetype for layer

# Example of a minimum solution:
# LOG_ROW = '"{now}";"{uri}";"{stype}"\n'

# Example of a comprehensive solution:
# LOG_ROW = '"{now}";"{host}";"{login}";"{name}";"{uri}";"{stype}"\n'

LOG_ROW = '"{now}";"{host}";"{login}";"{name}";"{uri}";"{stype}"\n'

# Error message written to the QGIS log if the external log can't be opened
ERR_MESS = 'Logfil: {} kunne ikke åbnes'

# Tab in QGIS log to write error message
ERR_TAB = 'Logning'

lfError = False

def onLayersAdded(layers):

    global lfError
    
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    login = getlogin()
    host = gethostname()

    strx = ''
    
    for layer in layers:        
        name = ''
        uri = ''

        if layer:
            name = layer.name()
            datap = layer.dataProvider()

            if datap:            
                uri = datap.dataSourceUri()
        
                if isinstance(datap,QgsRasterDataProvider):
                    stype = 'raster'
                else:
                    stype = datap.storageType()

        strx += LOG_ROW.format(now=now, host=host, login=login, name=name, uri=uri, stype=stype)

    try:
        g = open(LOG_FILE, "a")
        g.write(strx)
        g.close()
        lfError = False

    except OSError:
        if not lfError: QgsMessageLog.logMessage(ERR_MESS.format(LOG_FILE), ERR_TAB, Qgis.Warning, False)
        lfError = True

QgsProject.instance().layersAdded.connect(onLayersAdded)
