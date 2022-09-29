#!/bin/python3

import os
import json
import link_sftp
import rename
import gestion_log
from datetime import datetime
from time import strftime

# Ouverture du JSON & importation des clés
with open('configuration.json', 'r') as js:
    gestion_log.Ecrire_rapport("Ouverture du fichier de configuration")
    config = json.load(js)

historisation_b = config["historisation"]
periode = config["perdiode_suppression"]
ip = config["ip_machine"]
user = config["user_sftp"]
mdp = config["mdp_sftp"]
gestion_log.Ecrire_rapport("Fermeture du fichier de configuration")
js.close()


def enregistrement(file, ip, user, mdp):
    if historisation_b:
        creation_date = rename.rename(file, ".zip")
        link_sftp.send_file(ip, user, mdp, creation_date)
        os.system(
            f"echo 'python3 suppression_sftp.py {creation_date}' | at now +{periode} days")
        gestion_log.Ecrire_rapport("Suppression du fichier distant : "+creation_date+" prévue pour dans " + periode + " jours" )
        os.system(f'rm {creation_date}')
    return


