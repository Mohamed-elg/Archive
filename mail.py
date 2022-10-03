#!/bin/python3

import json
from email.message import EmailMessage
import smtplib
import ssl
from datetime import datetime
from time import strftime
import gestion_log


def mail_send(reussi=True):
    """Permet d'envoyer le mail"""
    # Lecture du fichier de configuration
    with open('configuration.json', 'r') as js:
        gestion_log.Ecrire_rapport("Ouverture du fichier de configuration")
        config = json.load(js)
    email = config["mail"]["email"]
    key = config['mail']["key"]
    gestion_log.Ecrire_rapport(
        "Fermeture du fichier de configuration")
    destinataires = config['mail']["destinataires_mail"]
    bool_log = config['mail']["logs_mail"]
    gestion_log.Ecrire_rapport("Fermeture du fichier de configuration")
    serveur_smtp = config['mail']['serveur_smtp']
    port_smtp = config['mail']['port_smtp']

    if reussi:
        objet = config['mail']["Objet_mail_reussi"]
        js.close()
    else:
        objet = config['mail']["Objet_mail_echec"]
        js.close()

    mail = EmailMessage()
    mail['From'] = email
    mail['To'] = destinataires
    mail['Subject'] = objet

    gestion_log.Ecrire_rapport("Envoi du mail")

    if bool_log:
        gestion_log.Ecrire_rapport("Création de la pièce-jointe")
        body = 'Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.'
        mail.set_content(body)
        now = datetime.now()
        f = "logs/"+now.strftime("%Y-%m-%d")+".txt"

        mail.add_attachment(open(f, 'rb').read(), 'text', 'plain',
                            filename='Rapport.txt')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(serveur_smtp, port_smtp, context=context) as smtp:
        smtp.login(email, key)
        smtp.sendmail(mail['From'], mail["To"].split(","), mail.as_string())
        smtp.close()
    return
