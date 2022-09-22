#!/bin/python3

import urllib.request


# Récupération de l'archive zip
#!Adapter l'adresse IP en fonction du réseau
url = 'http://192.168.23.226/test_export.sql.zip'
urllib.request.urlretrieve(url, 'test_export.zip')

# Décompression de l'archive
