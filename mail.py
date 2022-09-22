#!/bin/python3

import json
from email.message import EmailMessage
import smtplib
import ssl

# Ouverture du JSON & importation des clés
with open('mail.json', 'r') as js:
    key = json.load(js)

email = str(key["email"])
password = str(key["password"])

js.close()

with open('configuration.json', 'r') as js:
    key = json.load(js)

destinataires = key["destinataires_mail"]

js.close()

mail = EmailMessage()
mail['From'] = email
mail['To'] = ",".join(destinataires)
mail['Subject'] = 'Envoi réussi'
body = 'Hello world'
mail.set_content(body)


def mail_send(email, password, mail):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(mail['From'], mail['To'], mail.as_string())
    return


mail_send(email, password, mail)
