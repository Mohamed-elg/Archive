#!/bin/python3

from ast import Mod
from os import rename #? 
import subprocess
import mail
import modification_zip
import link_sftp
import gestion_log
import rename

# Programme principal à exécuter périodiquement
# gestion_log.creer_rapport()


# 1 - Téléchargement & décompression du fichier
gestion_log.Ecrire_rapport("Lancement du programme principal")
try:
    subprocess.call("./file_apache.sh")
    gestion_log.Ecrire_rapport("Fichier téléchargé et dézziper")

# 2 - Contrôle du zip
     

    if(modification_zip.modification(a,file)):
        
        link_sftp.rm_file(ip, user, mdp, file)
        gestion_log.Ecrire_rapport("suppression de l'ancienne version fichier")
        rename.rename("")
        modification_zip.compress_to_tar(file)
        link_sftp.send_file(ip, user, mdp,file)
        gestion_log.Ecrire_rapport("Ajout de la nouvelle version du fichier")

        


# 2- Renommer le fichier avec le bon format & recompresser


# 3 - Envoi d'un mail avec/sans rapport
    gestion_log.Ecrire_rapport("Programme terminé")
    mail.mail_send()

except:
    gestion_log.Ecrire_rapport("Echec du programme")
    mail.mail_send(False)
