#!/bin/python3

import os
from datetime import datetime
import gestion_log

# Permet de rennomer un fichier par sa date de création


def rename(file):
    new_name = str(date.today())
    os.rename(file, new_name+'.'+file.split('.')[1])
    gestion_log.Ecrire_rapport(
        f"Fichier : {file} renommé en : {new_name}")
    return new_name+'.'+file.split('.')[1]
