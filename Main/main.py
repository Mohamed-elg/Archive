#!/bin/python3

from ast import Mod
import subprocess
import mail
import modification_zip
import link_sftp
import gestion_log
import historisation
import rename
import json

# Programme principal à exécuter périodiquement

file_dl = 'test100.sql'
file = 'test200.sql'

# 1 - Téléchargement & décompression du fichier
gestion_log.Ecrire_rapport("Lancement du programme principal")
try:
    subprocess.call("./file_apache.sh")
    gestion_log.Ecrire_rapport("Fichier téléchargé et dézziper")

# 2 - Contrôle du zip

    # cas ou le fichier n'a pas changé
    if (not modification_zip.modification(file_new, file)):
        try:
            gestion_log.Ecrire_rapport("suppression de l'ancien fichier")
            # ! j'ai changer la condition du if
            link_sftp.rm_file(file)
        except:
            pass


# 2- Renommer le fichier avec le bon format & recompresser
        gestion_log.Ecrire_rapport("Ajout du nouveau fichier")
        file_new = rename.rename(file_new)
        file_dl = file_new
        file_new = modification_zip.compress_to_tar(file_new)
        historisation.enregistrement(file_new)

    else:
        gestion_log.Ecrire_rapport("Ajout d'une nouvelle version du fichier")
        file_new = rename.rename(file_new)
        file_dl = file_new
        file_new = modification_zip.compress_to_tar(file_new)
        historisation.enregistrement(file_new)


# 3 - Envoi d'un mail avec/sans rapport
    gestion_log.Ecrire_rapport("Programme terminé avec succès")
    if read_configuration.Envoi_mail:
        mail.mail_send()

except:
    gestion_log.Ecrire_rapport("Echec du programme")
    if read_configuration.Envoi_mail:
        mail.mail_send(False, read_configuration.objet_echec)
