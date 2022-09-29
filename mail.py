#!/bin/python3

import json
from email.message import EmailMessage
from datetime import datetime
from time import strftime
import gestion_log
import yagmail


def Envoi_mail():
    if bool_log:
        # Ouverture du JSON & importation des clés
        with open('mail.json', 'r') as js:
            gestion_log.Ecrire_rapport("Ouverture du fichier de configuration du mail")
            id = json.load(js)
        email = id["email"]
        password = id["password"]
        gestion_log.Ecrire_rapport("Fermeture du fichier de configuration du mail")
        js.close()


        # ouverture du fichier de configuration
        with open('configuration.json', 'r') as js:
            gestion_log.Ecrire_rapport("Ouverture du fichier de configuration")
            config = json.load(js)
        destinataires = config["destinataires_mail"]
        objet = config["Objet_mail"]
        bool_log = config["logs_mail"]
        gestion_log.Ecrire_rapport("Fermeture du fichier de configuration")
        js.close()

        gestion_log.Ecrire_rapport("Connexion au serveur SMTP de google")
        yag = yagmail.SMTP(email, password)
        now = datetime.now()
        contents = [
        "Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.", 'logs/'+now.strftime("%m-%d-%Y")+'.txt'
        ]
        yag.send(destinataires, objet, contents)

