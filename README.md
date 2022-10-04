# **Mini-Projet : utilitaire d'archive**

## **Guide d'installation & d'utilisation**

<br>

## Démarche & choix retenus

- Machine virtuel : Linux Debian 11 (bullseye)
- Language : Python3 et Bash
- Serveur web : Apache
- Méthode de transfert : SFTP ave openSSH
- Automatisation : Crontab
- Méthode email : SMTPS avec gmail
- Fichier de configuration : format json (pour la lisibilité)

<br>

![alt text](neofetch.png)

## Tâches restantes :

- Compression en .zip
- Fichier de log
- Correctifs
- Documentation utilisateur d'installation
- Mémoire technique

## Prérequis :

1. auDes adresses IP statiques
2. Exécuter en _sudo_ le fichier _dependances.sh_
3. Exécuter en _sudo_ le fichier _install_Web_Server.sh_ pour l'installation du serveur web
4. Il faut se connecter manuellement en SFTP la première fois avec la machine

## Automatisation de l'exécution du script principal :

**Il faut exécuter le fichier _automatisation_crontab.sh_ après chaque modification de la période ou du chemin du programme
Arguments possibles pour le champs _période_ crontab**

- @reboot
- @yearly
- @annually
- @monthly
- @weekly
- @daily
- @midnight
- @hourly
