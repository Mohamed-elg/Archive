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
        creation_date = rename.rename(file, ".zip")
        link_sftp.send_file(ip, user, mdp, creation_date)
        os.system(
            f"echo 'python3 suppression_sftp.py {creation_date}' | at now +{periode} days")
        os.system(f'rm {creation_date}')
    return


enregistrement('test.zip', ip, user, mdp)
