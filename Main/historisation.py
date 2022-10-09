#!/bin/python3

import os
import json
import link_sftp
import rename
import read_configuration
import gestion_log

from datetime import datetime
from time import strftime


def enregistrement(file, ip=read_configuration.ip, user=read_configuration.user, mdp=read_configuration.mdp, chemin_p=read_configuration.chemin_prg):
    if read_configuration.historisation_b:
        link_sftp.send_file(file, ip, user, mdp)
        os.system(
            f"echo 'python3 {chemin_p}/suppression_sftp.py {file}' | at now +{read_configuration.periode} days")
        gestion_log.Ecrire_rapport(
            f"Suppression du fichier distant : {file} prévue dans {read_configuration.periode} jours")
        os.system(f'rm {file}')
    return
