#!/bin/python3

import pysftp
import json
import gestion_log

# Connexion et partage de fichier via le serveur SFTP
#!les logs et les chemins sont susceptibles de changer

with open('configuration.json', 'r') as js:
    config = json.load(js)
    gestion_log.Ecrire_rapport('Ouverture fichier de configuration')
ip = config["ip_machine"]
user = config["user_sftp"]
mdp = config["mdp_sftp"]

js.close()
gestion_log.Ecrire_rapport('Fermeture fichier de configuration')

def send_file(ip, user, mdp, file):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).put(
            file, f'/home/mohamed/Bureau/SFTP/{file}')
        print('Envoi réussi')
        gestion_log.Ecrire_rapport("Envoi de "+file " via SFTP réussi")
    except:
        print("Echec de l'envoi")
        gestion_log.Ecrire_rapport("ECHEC de l'envoi de " +file+" via SFTP")


def get_file(ip, user, mdp, file):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).get(
            f'/home/mohamed/Bureau/SFTP/{file}', file)
        print('Reception réussie')
        gestion_log.Ecrire_rapport("Récupération de " +file +" via SFTP réussie")
    except:
        print('Echec de la réception')
        gestion_log.Ecrire_rapport("ECHEC de la récupération de "+ file + " via SFTP")



def rm_file(ip, user, mdp, file):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).remove(
            f'/home/mohamed/Bureau/SFTP/{file}')
        print('Suppression réussie')
        gestion_log.Ecrire_rapport("Suppression du fichier distant : "+file+" réussie")
    except:
        print('Echec de la suppression')
        gestion_log.Ecrire_rapport("ECHEC de la suppression du fichier distant : "+file)


#send_file(ip, user, mdp, 'README.md')
#rm_file(ip, user, mdp, 'README.md')
