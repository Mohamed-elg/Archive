# Mini-Projet : utilitaire d'archive

## **Guide d'installation & d'utilisation**

<br>

## Démarche & choix retenus

- Machine virtuel : Linux Debian 11 (bullseye)
- Language : Python3 et Bash
- Serveur web : Apache
- Méthode de transfert : SFTP ave openSSH
- Automatisation : Cron
- Méthode email : SMTPS avec gmail
- Fichier de configuration : format json (pour la lisibilité)

![alt text](neofetch.png)

## Tâches restantes :

- Compression en .zip
- Fichier de log
- Commande CRON
- Correctifs
- Documentation utilisateur d'installation
- Mémoire technique

## Prérequis :

_commandes pip pour les installer_

    pip install pysftp
    sudo apt install at

- Des adresses IP statiques
- Il faut se connecter manuellement en SFTP la première fois avec la machine

## liens utiles :

CRON : https://crontab.guru/ pour les automatisations
