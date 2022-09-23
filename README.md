# Mini-Projet : utilitaire d'archive

## Démarche & choix retenus

- Machine virtuel : Linux Debian 11 (bullseye)
- Language : Python3 et Bash
- Serveur web : Apache
- Méthode de transfert : SFTP ave openSSH
- Automatisation : Cron
- Méthode email : SMTPS avec gmail
- Fichier de configuration : format json (pour la lisibilité)

## Tâches restantes

- Mettre en place le programme d'expiration
- Passer le serveur web en httpS
- Renommer les archives en AAAA-MM-JJ
- Historisation (avoir plusieurs version d'un même fichier)
- Fichier de log
- Commande CRON
- Correctifs
- PJ pour les mails
- Documentation utilisateur d'installation
- Mémoire technique

## Modules prérequis:

_commandes pip pour les installer_

    pip install pysftp

## liens utiles :

CRON : https://crontab.guru/ pour les automatisations
