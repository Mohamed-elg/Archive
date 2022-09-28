#!/bin/python3

import os
import json
import link_sftp
import rename

# Ouverture du JSON & importation des clés
with open('configuration.json', 'r') as js:
    config = json.load(js)

historisation_b = config["historisation"]
periode = config["perdiode_suppression"]
ip = config["ip_machine"]
user = config["user_sftp"]
mdp = config["mdp_sftp"]
js.close()


def enregistrement(file, ip, user, mdp):
    if historisation_b:
        rename.rename(file, ".zip")
        link_sftp.send_file(ip, user, mdp, file)
        os.system(f"at now +{periode} -f suppression_sftp.py {file}")
    return
