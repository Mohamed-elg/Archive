#!/bin/python3

import pysftp
import read_configuration
import gestion_log

# Connexion et partage de fichier via le serveur SFTP


def send_file(file, ip=read_configuration.ip, user=read_configuration.user, mdp=read_configuration.mdp, chemin=read_configuration.chemin_sftp):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).put(
            file, f'{chemin}/{file}')
        print('Envoi réussi')
        gestion_log.Ecrire_rapport(f"Envoi de {file} via SFTP réussi")
    except:
        print("Echec de l'envoi SFTP")
        gestion_log.Ecrire_rapport("echec de l'envoi de " + file+" via SFTP")
    return


def get_file(file, ip=read_configuration.ip, user=read_configuration.user, mdp=read_configuration.mdp, chemin=read_configuration.chemin_sftp):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).get(
            f'{chemin}/{file}', file)
        print('Reception réussie')
        gestion_log.Ecrire_rapport(
            "Récupération de " + file + " via SFTP réussie")
        return True
    except:
        print('Echec de la réception SFTP')
        gestion_log.Ecrire_rapport(
            "Echec de la récupération de " + file + " via SFTP")
        return False


def rm_file(file, ip=read_configuration.ip, user=read_configuration.user, mdp=read_configuration.mdp, chemin=read_configuration.chemin_sftp):
    """File --> nom du fichier + extension"""
    try:
        pysftp.Connection(ip, username=user, password=mdp, port=22).remove(
            f'{chemin}/{file}')
        print('Suppression réussie')
    except:
        pass
    return
