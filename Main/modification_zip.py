#!/bin/python3

from unittest import result
# import pour la comparaison de fichier sql
from difflib import Differ
# Modification de fichier zip
from zipfile import ZipExtFile, ZipFile

import os

# Modification à l'aide de la fonction diff

def modification(a, b):
    r = os.popen("if diff -q " + a + " " + b + " ; then echo '0' ; else echo '1' ; fi ;").read()
    r = r.split()

    if(r[0] == '0'):
        print("Pas de modification nécéssaire")
        return(False)
    else:
        print("Modification du fichier")
        return(True)


def zip_(file):
    file_name = file.split('.')  # on découpe le nom et l'extension

    with ZipFile(file_name[0] + '.zip', 'w') as myzip:
        myzip.write(file)  # on écrit le fichier de départ dans l'archive
    return


def decompress(a):
    with ZipFile(a, 'r') as myzip:
        myzip.extractall()  # il est enregistré dans un dossier du nom de a sans l'extension

    return


def compress_to_tar(a):
    file_name = a.split('.')
    os.system("tar -cvzf " + file_name[0] + ".tgz "+a)
    return (file_name[0]+'.tgz')
