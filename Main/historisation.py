#!/bin/python3

import os
import json
import link_sftp
import rename
import read_configuration

from datetime import datetime
from time import strftime


def enregistrement(file, ip=read_configuration.ip, user=read_configuration.user, mdp=read_configuration.user):
    if read_configuration.historisation_b:
        creation_date = rename.rename(file, ".zip")
        link_sftp.send_file(ip, user, mdp, creation_date)
        os.system(
            f"echo 'python3 suppression_sftp.py {creation_date}' | at now +{periode} days")
        gestion_log.Ecrire_rapport(
            f"Suppression du fichier distant : {creation_date} prévue pour dans {periode} jours")
        os.system(f'rm {creation_date}')
    return
