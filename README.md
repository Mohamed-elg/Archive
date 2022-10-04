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

## Mise en place du serveur web avec chiffrement SSL

**Choix retenu pour le serveur : Apache2**

- Mise en place du serveur Apache:

  1. Installer les paquets/dépendances nécessaire en Executant en _sudo_ le fichier _depandance.sh_
  2. Executer en _sudo_ le fichier _publish_WebServer.sh_ et entrer en argument le fichier à upload qui doit être dans le même répertoire que _publish_WebServer.sh_
     <br>

- Mise en place du chiffrement SSL :

  3. Créer un répertoire pour les certificats avec _sudo mkdir /etc/apache2/certs_ puis se placer dedans _cd /etc/apache2/certs_
  4. Lancer la génération du certificat avec _sudo openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out apache.crt -keyout apache.key_
  5. Les fichiers _apache.crt_ et _apache.key_ ont normalement été crée dans le repertoire _certs_
  6. Changer la configuration d'Apache avec _sudo nano /etc/apache2/sites-enabled/000-default.conf_ et ajouter :

  ```
  <VirtualHost *:443>
      ServerAdmin webmaster@localhost
      DocumentRoot /var/www/html
      ErrorLog ${APACHE_LOG_DIR}/error.log
      CustomLog ${APACHE_LOG_DIR}/access.log combined
      SSLEngine on
      SSLCertificateFile /etc/apache2/certs/apache.crt
      SSLCertificateKeyFile /etc/apache2/certs/apache.key
  </VirtualHost>
  ```

  7. Pour automatiser la redirection en HTTPS ajouter dans la règle du port 80 :

  ```
      RewriteEngine on
      RewriteCond %{HTTPS} !=on
      RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R=301,L]
  ```

  Assurez vous d'être dans le bloc

  ```
  <VirtualHost *:80>
      ...
  </VirtualHost>
  ```

  8. Relancer le serveur apache avec _sudo systemctl restart apache2_

Le serveur web est opérationnel, on y accède avec https://[IP]

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
