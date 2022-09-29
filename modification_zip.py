#!/bin/python3

from unittest import result
# import pour la comparaison de fichier sql
from difflib import Differ
#Modification de fichier zip
from zipfile import ZipFile

import os

def modification(a,b):
    """"Les arguments sont les chemins des fichiers Fonction qui vérifie les modifications entre les fichiers sql, un fichier est créée avec toute les modifications : result et les modifs contiennent des (+/-), et on cherche dans ce fichier la présence de +. """
    d = Differ() 
    result = list(d.compare(open(a, 'r').readlines(), open(b, 'r').readlines())) # fichier résultant de la comparaison des deux .sql
    for line in result:                     #on vérifie ligne par ligne
        if ('+' in line):                   #si le charactère + est trouvé -> il y a eu une modification 
            print("find a modification")
            return (True)
    print("no modification found")
    return (False)


def zip_(file):
    file_name = file.split('.') #on découpe le nom et l'extension

    with ZipFile(file_name[0] + '.zip', 'w') as myzip:
        myzip.write(file) # on écrit le fichier de départ dans l'archive  
    return


def decompress(a):
    with ZipFile(a, 'r') as myzip:
        myzip.extractall() # il est enregistré dans un dossier du nom de a sans l'extension

    return 


def compress_to_tar(a):
    file_name = a.split('.')
    os.system("tar -cvzf " + file_name[0] + ".tgz .")
    return

# A revérifier, il permet la décompression du fichier
# def decompress_tar(a):
#     os.system("tar -xvzf " + a)
#     return


# decompress_tar("testa.tgz")