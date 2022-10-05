#!/bin/python3

from unittest import result
# import pour la comparaison de fichier sql
from difflib import Differ
#Modification de fichier zip
from zipfile import ZipExtFile, ZipFile

import os

#Modification par lecture ligne par ligne et comparaison avec 
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


# Test d'une nouvelle fonction compare depuis le terminal à revérifier
def sql_compare(a,b):
    os.system("diff -c" + a + " " + b) 
    return

# A revérifier, il permet la décompression du fichier
# def decompress_tar(a):
#     os.system("tar -xvzf " + a)
#     return

# decompress_tar("testa.tgz")


# Ensemble de TEST réalisé 04/10/22 VALIDE

#TEST zip_ : .sql devient un .zip, valide
#       exemple de test : zip_('test100-copy.sql')
#TEST decompress_ : decompresse un fichier .zip, valide
#       exemple de test : decompress('test100-copy.zip')
#TEST compress_to_tar , compresse un fichier en .tgz, valide
#       exemple de test : compress_to_tar('test100-copy.sql')
#TEST modification : compare deux fichiers sql entre eux et indique s'il y a une modificaiton,
    #exemple de test :modification('test100-copy.sql','test100-copy2.sql') , valide 
