#!/bin/python3

from unittest import result

# import pour la comparaison de fichier sql
from difflib import Differ

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

#modification('test100.sql','test100-copy.sql')

from zipfile import ZipFile

def zip_(file):
    file_name = file.split('.') #on découpe le nom et l'extension

    with ZipFile(file_name[0] + '.zip', 'w') as myzip:
        myzip.write(file) # on écrit le fichier de départ dans l'archive  


    return(file)


#zip_('name_file.txt')
