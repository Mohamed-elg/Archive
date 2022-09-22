#!/bin/python3

import urllib.request
import zipfile
import json


with open('configuration.json', 'r') as js:
    key = json.load(js)

url = key["url_fichier"]

js.close()

# Récupération de l'archive zip
#!Changer le nom du fichier
urllib.request.urlretrieve(url, 'test_export.zip')

# Décompression de l'archive
# Pas d'argument pour extractall - -> dans le répertoire courant
zipfile.ZipFile('test_export.zip', 'r').extractall()
