#!/bin/python3

import json
from email.message import EmailMessage
import smtplib
import ssl

# Ouverture du JSON & importation des clés
with open('mail.json', 'r') as js:
    key = json.load(js)

email = key["email"]
password = key["password"]

js.close()

# ouverture du fichier de configuration
with open('configuration.json', 'r') as js:
    key = json.load(js)

destinataires = key["destinataires_mail"]
objet = key["Objet_mail"]

js.close()
# TODO : Mettre le bon chemin pour les logs
with open("README.md", 'rb') as rm:
    readme = rm.read()

mail = EmailMessage()
mail['From'] = email
mail['To'] = destinataires
mail['Subject'] = objet
body = 'Bonjour,\nVous trouverez en pièce jointe, le rapport des logs.\n\nCeci est un message automatique.'
mail.set_content(body)
# Format pdf obligatoirement
mail.add_attachment(readme, 'application', 'pdf', filename='Rapport')
print(mail.as_string())

#! L'envoi à plusieurs destinataires ne marche pas


def mail_send(email, password, mail):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(mail['From'], mail['To'], mail.as_string())
        smtp.close()
    return


mail_send(email, password, mail)
