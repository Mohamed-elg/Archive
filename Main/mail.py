#!/bin/python3

from email.message import EmailMessage
import smtplib
import ssl
from datetime import datetime
from time import strftime
import read_configuration
import gestion_log


def mail_send(reussi=True, objet=read_configuration.objet_reussi):
    """Permet d'envoyer le mail"""
    mail = EmailMessage()
    mail['From'] = read_configuration.email
    mail['To'] = read_configuration.destinataires
    mail['Subject'] = objet

    gestion_log.Ecrire_rapport("Envoi du mail")

    if read_configuration.bool_log:
        gestion_log.Ecrire_rapport("Création de la pièce-jointe")
        body = 'Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.'
        mail.set_content(body)
        now = datetime.now()
        f = "logs/"+now.strftime("%Y-%m-%d")+".log"

        mail.add_attachment(open(f, 'rb').read(), 'text', 'plain',
                            filename='Rapport.log')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(read_configuration.serveur_smtp, read_configuration.port_smtp, context=context) as smtp:
        smtp.login(read_configuration.email, read_configuration.key)
        smtp.sendmail(mail['From'], mail["To"].split(","), mail.as_string())
        smtp.close()
    return
