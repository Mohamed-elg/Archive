#!/bin/python3

import json
from email.message import EmailMessage
import smtplib
import ssl
from datetime import datetime
from time import strftime
import gestion_log

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

#TODO Modifier le fichier de log (txt --> PDF)
def mail_format(destinataires, objet, bool_log):
    """Permet de mettre en forme le mail"""
    mail = EmailMessage()
    mail['From'] = email
    mail['To'] = destinataires
    mail['Subject'] = objet
    if bool_log:
        body = 'Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.'
        mail.set_content(body)
        # Format pdf obligatoirement
        now = datetime.now()
        mail.add_attachment("logs/"+now.strftime("%m-%d-%Y")+".txt", 'application', 'pdf', filename='Rapport')
    return mail


def mail_send(email, password):
    """Permet d'envoyer le mail"""
    mail = mail_format(destinataires, objet, bool_log)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        gestion_log.Ecrire_rapport("Envoi du mail")
        smtp.sendmail(mail['From'], mail['To'], mail.as_string())
        smtp.close()
    return

#! L'envoi à plusieurs destinataires ne marche pas
#mail_send(email, password)
