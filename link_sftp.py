import pysftp
import json

# Connexion et partage de fichier via le serveur SFTP
#!les logs et les chemins sont susceptibles de changer

with open('configuration.json', 'r') as js:
    key = json.load(js)

ip = key["ip_machine"]

js.close()

user = 'mohamed'
mdp = '0905'


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


#send_file(ip, user, mdp, 'README.md')
