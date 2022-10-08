#!/bin/python3

import os
import json
import link_sftp
import rename
import read_configuration
import gestion_log

from datetime import datetime
from time import strftime


def enregistrement(file, ip=read_configuration.ip, user=read_configuration.user, mdp=read_configuration.mdp):
    if read_configuration.historisation_b:
        link_sftp.send_file(file, ip, user, mdp)
        os.system(
            f"echo 'python3 suppression_sftp.py {file}' | at now +{periode} days")
        gestion_log.Ecrire_rapport(
            f"Suppression du fichier distant : {file} prévue pour dans {periode} jours")
        os.system(f'rm {file}')
    return
