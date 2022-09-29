#!/bin/python3

import link_sftp
import json
import sys
import gestion_log

with open('configuration.json', 'r') as js:
    gestion_log.Ecrire_rapport("Ouverture du fichier de configuration")
    config = json.load(js)
    ip = config["ip_machine"]
    user = config["user_sftp"]
    mdp = config["mdp_sftp"]
    gestion_log.Ecrire_rapport("Fermeture du fichier de configuration")
js.close()

link_sftp.rm_file(ip, user, mdp, sys.argv[1])
