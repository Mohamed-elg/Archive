#!/bin/bash

import os
import json
import link_sftp
import rename

# Ouverture du JSON & importation des clés
with open('configuration.json', 'r') as js:
    id = json.load(js)
historisation_b = id["historisation"]
perdiode = id["perdiode_suppression"]
js.close()

with open('configuration.json', 'r') as js:
    config = json.load(js)
ip = config["ip_machine"]
user = config["user_sftp"]
mdp = config["mdp_sftp"]
js.close()


def enregistrement(file, ip, user, mdp):
    if historisation_b:
        rename.rename(file, ".zip")
        link_sftp.send_file(ip, user, mdp, file)
    return
