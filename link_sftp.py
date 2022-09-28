#!/bin/python3

import pysftp
import json

# Connexion et partage de fichier via le serveur SFTP
#!les logs et les chemins sont susceptibles de changer

with open('configuration.json', 'r') as js:
    config = json.load(js)

ip = config["ip_machine"]
user = config["user_sftp"]
mdp = config["mdp_sftp"]

js.close()


def send_file(ip, user, mdp, file):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).put(
            file, f'/home/mohamed/Bureau/SFTP/{file}')
        print('Envoi réussi')
    except:
        print("Echec de l'envoi")


def get_file(ip, user, mdp, file):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).get(
            f'/home/mohamed/Bureau/SFTP/{file}', file)
        print('Reception réussie')
    except:
        print('Echec de la réception')

#todo : tester
def rm_file(ip, user, mdp, file):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).remove(
            f'/home/mohamed/Bureau/SFTP/{file}', file)
        print('Suppression réussie')
    except:
        print('Echec de la suppression')


#send_file(ip, user, mdp, 'README.md')
