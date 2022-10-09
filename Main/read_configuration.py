import json
import gestion_log


with open('configuration.json', 'r') as js:
    config = json.load(js)

ip = config["ip_machine"]
user = config["user_sftp"]
mdp = config["mdp_sftp"]

Envoi_mail = config['mail']['Envoi_mail']
email = config["mail"]["email"]
key = config['mail']["key"]
destinataires = config['mail']["destinataires_mail"]
bool_log = config['mail']["logs_mail"]

serveur_smtp = config['mail']['serveur_smtp']
port_smtp = config['mail']['port_smtp']

objet_reussi = config['mail']["Objet_mail_reussi"]
objet_echec = config['mail']["Objet_mail_echec"]

historisation_b = config['historisation']
periode = config['periode_suppression']

chemin_sftp = config['chemin_sftp']
chemin_prg = config['chemin_Programme']
