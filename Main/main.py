#!/bin/python3

from datetime import date
from datetime import timedelta
from ast import Mod
import os
import subprocess
import mail
import modification_zip
import link_sftp
import gestion_log
import historisation
import rename
import json
import read_configuration

# Programme principal à exécuter périodiquement


# 1 - Téléchargement & décompression du fichier depuis le serveur web et le fichier de la veille depuis le serveur SFTP
gestion_log.Ecrire_rapport("Lancement du programme principal")
try:
    file_dl = 'test100.sql'
    subprocess.call("./file_apache.sh")
    gestion_log.Ecrire_rapport("Fichier téléchargé et dézziper")
    file_old = str(date.today()-timedelta(days=1))+'.tgz'
    if link_sftp.get_file(file_old):
        os.system('tar zxvf '+file_old+' && rm '+file_old)
        file_old = str(date.today()-timedelta(days=1))+'.sql'


# 2 - Contrôle du fichier SQL

        if (modification_zip.modification(file_dl, file_old)):
            gestion_log.Ecrire_rapport("Ajout du nouveau fichier")
            # 3- Renommer le fichier avec le bon format & recompresser puis envoyer en SFTP sur le serveur distant
            file_dl = rename.rename(file_dl)
            file_new = modification_zip.compress_to_tar(file_dl)
            file_new = rename.rename(file_new)
            historisation.enregistrement(file_new)
        # cas ou le fichier n'a pas changé
        else:
            gestion_log.Ecrire_rapport(
                'Le fichier est le même que celui de la veille, aucune action nécessaire')
    else:
        gestion_log.Ecrire_rapport("Ajout du nouveau fichier")
        file_dl = rename.rename(file_dl)
        file_new = modification_zip.compress_to_tar(file_dl)
        file_new = rename.rename(file_new)
        historisation.enregistrement(file_new)
    os.system('rm '+file_dl+' && rm '+file_old)

# 4 - Envoi d'un mail avec/sans rapport
    gestion_log.Ecrire_rapport("Programme terminé avec succès")
    if read_configuration.Envoi_mail:
        mail.mail_send()

except:
    gestion_log.Ecrire_rapport("Echec du programme")
    if read_configuration.Envoi_mail:
        mail.mail_send(False, read_configuration.objet_echec)
