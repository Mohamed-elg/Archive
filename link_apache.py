#!/bin/python3

#!CE FICHIER VA ETRE SUPPRIME
import urllib.request
import zipfile
import json
import gestion_log


with open('configuration.json', 'r') as js:
    gestion_log.Ecrire_rapport("Ouverture du fichier de configuration")
    key = json.load(js)

url = key["url_fichier"]
gestion_log.Ecrire_rapport("Fermeture du fichier de configuration")
js.close()

# Récupération de l'archive zip
#!Changer le nom du fichier
gestion_log.Ecrire_rapport("Récupération de l'archive sur le serveur apache")
urllib.request.urlretrieve(url, 'test_export.zip')

# Décompression de l'archive
# Pas d'argument pour extractall - -> dans le répertoire courant
zipfile.ZipFile('test_export.zip', 'r').extractall()
gestion_log.Ecrire_rapport("Décompression de l'archive")
