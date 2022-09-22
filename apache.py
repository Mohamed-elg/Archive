#!/bin/python3

import urllib.request
import zipfile

# Récupération de l'archive zip
#!Adapter l'adresse IP en fonction du réseau
url = 'http://172.20.10.2/test_export.sql.zip'
urllib.request.urlretrieve(url, 'test_export.zip')

# Décompression de l'archive
# Pas d'argument pour extractall - -> dans le répertoire courant
zipfile.ZipFile('test_export.zip', 'r').extractall()
