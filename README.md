# **Mini-Projet : utilitaire d'archive**

## **Guide d'installation & d'utilisation**

<br>

## **I - Configuration**

- Machine virtuel : Linux Debian 11 (bullseye)
- Language : Python3 et Bash
- Serveur web : Apache
- Méthode de transfert : SFTP ave openSSH
- Automatisation : Crontab
- Méthode email : SMTPS avec gmail
- Fichier de configuration : format json

<br>

![alt text](neofetch.png)

## **II - Prérequis :**

1. Des adresses IP statiques.
2. Exécuter en _sudo_ le fichier _dependances.sh_.
3. Exécuter en _sudo_ le fichier _install_Web_Server.sh_ pour l'installation du serveur web.

## **III - Mise en place du serveur web avec chiffrement SSL**

**Choix retenu pour le serveur : Apache2**

<br>
Mise en place du serveur Apache:

1. Installer les paquets/dépendances nécessaire en Executant en _sudo_ le fichier _depandance.sh_ sur chacune des machines.
2. Executer en _sudo_ le fichier _publish_WebServer.sh_ et entrer en argument le fichier à upload qui doit être dans le même répertoire que _publish_WebServer.sh_.
3. Mettre les bon paramètres dans le fichier de configuration _configuration.json_ et le placer avec le script principal.

<br>
Mise en place du chiffrement SSL :

1. Créer un répertoire pour les certificats avec _sudo mkdir /etc/apache2/certs_ puis se placer dedans _cd /etc/apache2/certs_.
2. Lancer la génération du certificat avec _sudo openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out apache.crt -keyout apache.key_.
3. Les fichiers _apache.crt_ et _apache.key_ ont normalement été crée dans le repertoire _certs_.
4. Changer la configuration d'Apache avec _sudo nano /etc/apache2/sites-enabled/000-default.conf_ et ajouter :

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

5. Pour automatiser la redirection en HTTPS ajouter dans la règle du port 80 :

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

6. Relancer le serveur apache avec _sudo systemctl restart apache2_.

Le serveur web est opérationnel, on y accède avec https://[IP].

## **IV - Mise en place du serveur de destination**

**Choix retenu : Protocole SFTP**
<br>
**Sur la machine qui servira de stockage :**

1. Installer OpenSSH avec la commande _sudo apt install openssh-server_
2. Créer un répertoire et ajouter son chemin dans le fichier de configuration
3. Se connecter une première fois à la machine distante en sftp depuis la machine qui exécutera le script principal en entrant la commande _sudo sftp [user]@[ip]_ puis entrer le mot de passe de l'utilisateur puis autoriser la connexion. Vous êtes maintenant connecté en SFTP à la machine qui hébergera vos archives, vous pouvez fermer le terminal.

## **V - Automatisation de l'exécution du script principal :**

**Il faut exécuter le fichier _automatisation_crontab.sh_ après chaque modification de la période ou du chemin du programme
Arguments possibles pour le champs _période_ dans le fichier configuration.**

- @reboot
- @yearly
- @annually
- @monthly
- @weekly
- @daily
- @midnight
- @hourly
