from qgis.core import QgsProject, QgsMessageLog, Qgis, QgsRasterDataProvider
from datetime import datetime
from os import getlogin
from os.path import exists
from socket import gethostname

# Location of log file - Prefereably a network file. Every QGIS use has to have write access to this file
LOG_FILE = 'd:/tmp/loglag.csv'

# Error message wriiten to the QGIS log if the external log can't be opened
MESS = 'Logfil: {} kunne ikke åbnes'

# Tab in QGIS log to write error message
TAB = 'Logning'

error = False

def onLayersAdded(layers):

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
                
        # What to log is defined by the GIS administrator

        # Example for a minimum solution:
        # strx += '"{}";"{}";"{}"\n'.format(now, uri, stype)

        # Example for a comprehensive solution:
        # strx += '"{}";"{}";"{}";"{}";"{}";"{}"\n'.format(now, host, login, name, uri, stype)

        strx += '"{}";"{}";"{}";"{}";"{}";"{}"\n'.format(now, host, login, name, uri, stype)

    try:
        g = open(LOG_FILE, "a")
        g.write(strx)
        g.close()
        error = False

    except OSError:
        if not error: QgsMessageLog.logMessage(MESS.format(LOG_FILE), TAB, Qgis.Warning, False)
        error = True

QgsProject.instance().layersAdded.connect(onLayersAdded)
