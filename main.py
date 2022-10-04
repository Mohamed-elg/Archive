#!/bin/python3

import subprocess
import mail
import modification_zip
import link_sftp
import gestion_log

# Programme principal à exécuter périodiquement
# gestion_log.creer_rapport()


# 1 - Téléchargement & décompression du fichier
gestion_log.Ecrire_rapport("Lancement du programme principal")
try:
    subprocess.call("./file_apache.sh")
    gestion_log.Ecrire_rapport("Fichier téléchargé et dézziper")

# 2 - Contrôle du zip


# 2- Renommer le fichier avec le bon format & recompresser


# 3 - Envoi d'un mail avec/sans rapport
    gestion_log.Ecrire_rapport("Programme terminé")
    mail.mail_send()

except:
    gestion_log.Ecrire_rapport("Echec du programme")
    mail.mail_send(False)
