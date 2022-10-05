#!/bin/python3

import os
from datetime import datetime
import gestion_log

# Permet de rennomer un fichier par sa date de création


def rename(file):
    stat = os.stat(file)
    creation_date = str(datetime.fromtimestamp(stat.st_mtime))[0:10]
    os.rename(file, creation_date+file.split('.')[1])
    gestion_log.Ecrire_rapport(
        f"Fichier : {file} renommé en : {creation_date}")
    return creation_date+file.split('.')[1]
