#!/bin/python3

from unittest import result
import urllib.request
import zipfile

#import pour la comparaison de fichier sql
from difflib import Differ
from pprint import pprint 

# Récupération de l'archive zip
#!Adapter l'adresse IP en fonction du réseau
# url = 'http://192.168.23.226/test_export.sql.zip'
# urllib.request.urlretrieve(url, 'test_export.zip')

# Décompression de l'archive
# Pas d'argument pour extractall --> dans le répertoire courant
# zipfile.ZipFile('test_export.zip', 'r').extractall()

d = Differ() 
result = list(d.compare(open('test100.sql', 'r').readlines(), open('test100-copy.sql', 'r').readlines()))
pprint(result)

v = ['voiture','maison']

print(v.index('voiture'))
 
def modification(result):
    for line in result:
        if ('+' in line):
            print("find a modification")
            return(True)
    print("no modification found")
    return(False)

modification(result)


