#!/bin/python3

from ast import Mod
import subprocess
import mail
import modification_zip
import link_sftp
import gestion_log
import rename
import read_configuration
import json

# Programme principal à exécuter périodiquement

file_new = 'test100.sql.zip'
# 1 - Téléchargement & décompression du fichier
gestion_log.Ecrire_rapport("Lancement du programme principal")
try:
    subprocess.call("./file_apache.sh")
    gestion_log.Ecrire_rapport("Fichier téléchargé et dézziper")

# 2 - Contrôle du zip

    if (modification_zip.modification(file_new, file)):
        link_sftp.rm_file(file) #! Pourquoi on supprime sur le serveur stfp?
        gestion_log.Ecrire_rapport("suppression de l'ancienne version fichier")


# 2- Renommer le fichier avec le bon format & recompresser
        file_new = rename.rename(file_new)
        modification_zip.compress_to_tar(file_new)
        link_sftp.send_file(file_new) #! Plutôt utliser la fonction historisation.enregistrement() pour gérer la suppression auto ?
        gestion_log.Ecrire_rapport("Ajout de la nouvelle version du fichier")

# 3 - Envoi d'un mail avec/sans rapport
    gestion_log.Ecrire_rapport("Programme terminé")
    mail.mail_send()

except:
    gestion_log.Ecrire_rapport("Echec du programme")
    mail.mail_send(False, read_configuration.objet_echec)
