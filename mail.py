#!/bin/python3

import json
from email.message import EmailMessage
import smtplib
import ssl
from datetime import datetime
from time import strftime
import gestion_log


def Envoi_mail():

    # ouverture du fichier de configuration
    with open('configuration.json', 'r') as js:
        gestion_log.Ecrire_rapport("Ouverture du fichier de configuration")
        config = json.load(js)
    email = config["mail"]["email"]
    key = config['mail']["key"]
    gestion_log.Ecrire_rapport(
        "Fermeture du fichier de configuration du mail")
    destinataires = config['mail']["destinataires_mail"]
    objet = config['mail']["Objet_mail"]
    bool_log = config['mail']["logs_mail"]
    gestion_log.Ecrire_rapport("Fermeture du fichier de configuration")
    js.close()
    if bool_log:
        gestion_log.Ecrire_rapport("Connexion au serveur SMTP de google")
        yag = yagmail.SMTP(email, key)
        now = datetime.now()
        contents = [
            "Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.", 'logs/' +
            now.strftime("%Y-%m-%d")+'.txt'
        ]
        yag.send(destinataires, objet, contents)


# TODO Modifier le fichier de log (txt --> PDF)
def mail_send():
    """Permet de mettre en forme le mail"""
    with open('configuration.json', 'r') as js:
        gestion_log.Ecrire_rapport("Ouverture du fichier de configuration")
        config = json.load(js)
    email = config["mail"]["email"]
    key = config['mail']["key"]
    gestion_log.Ecrire_rapport(
        "Fermeture du fichier de configuration du mail")
    destinataires = config['mail']["destinataires_mail"]
    objet = config['mail']["Objet_mail"]
    bool_log = config['mail']["logs_mail"]
    gestion_log.Ecrire_rapport("Fermeture du fichier de configuration")
    js.close()
    mail = EmailMessage()
    mail['From'] = email
    mail['To'] = destinataires
    mail['Subject'] = objet
    if bool_log:
        gestion_log.Ecrire_rapport("Connexion au serveur SMTP de google")
        body = 'Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.'
        mail.set_content(body)
        # Format pdf obligatoirement
        now = datetime.now()
        mail.add_attachment("logs/"+now.strftime("%Y-%m-%d") +
                            ".txt", 'text', 'plain', filename='Rapport')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        gestion_log.Ecrire_rapport("Envoi du mail")
        smtp.sendmail(mail['From'], mail['To'], mail.as_string())
        smtp.close()
    return


mail_send()
