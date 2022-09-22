import pysftp

# Connexion et partage de fichier via le serveur SFTP
#! L'adresse IP,les logs et les chemins sont susceptibles de changer

ip = '172.20.10.2'
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
