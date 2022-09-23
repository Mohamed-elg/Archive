#!/bin/python3

import json
from email.message import EmailMessage
import smtplib
import ssl

# Ouverture du JSON & importation des clés
with open('mail.json', 'r') as js:
    id = json.load(js)
email = id["email"]
password = id["password"]
js.close()

# ouverture du fichier de configuration
with open('configuration.json', 'r') as js:
    config = json.load(js)
destinataires = config["destinataires_mail"]
objet = config["Objet_mail"]
log = config["logs_mail"]
js.close()

# TODO : Mettre le bon chemin pour les logs
with open("README.md", 'rb') as rm:
    readme = rm.read()
rm.close()


def mail_format(destinataires, objet, log):
    """Permet de mettre en forme le mail"""
    mail = EmailMessage()
    mail['From'] = email
    mail['To'] = destinataires
    mail['Subject'] = objet
    if log:
        body = 'Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.'
        mail.set_content(body)
        # Format pdf obligatoirement
        mail.add_attachment(readme, 'application', 'pdf', filename='Rapport')
    return mail


def mail_send(email, password):
    """Permet d'envoyer le mail"""
    mail = mail_format(destinataires, objet, log)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(mail['From'], mail['To'], mail.as_string())
        smtp.close()
    return

#! L'envoi à plusieurs destinataires ne marche pas
#mail_send(email, password)
