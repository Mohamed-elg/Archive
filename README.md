# **Mini-Projet : Utilitaire d'archive**

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

![alt text](neofetch.png)

<br>

## **II - Prérequis :**

0. Une machine sous Linux avec une distribution Debian ou basé sur Debian.
1. Les adresses IP des serveurs doivent être statique.
2. Exécuter en _sudo_ le fichier _dependances.sh_ afin de télécharger automatiquement toutes les dépendances nécessaires au bon fonction de l'utilitaire.

<br>

## **III - Configuration du script :**

Pour paramétrer l'éxecution du script, il faut modifier le fichier _configuration.json_ qui doit rester dans le répertoire _Main_ qui fait tourner le script principal. Nous allons expliciter les champs un à un.

- url_fichier : lien vers le fichier sur le serveur web
- ip_machine : Ip de la machine où l'on stocks les ficheirs en SFTP
- user_sftp : utilisateur de la machine SFTP
- mdp_sftp : mot de passe de la machien SFTP
- chemin_Programme : Chemin dans lequel se trouve le programme principal
- chemin_sftp : Chemin où seront stocké les fichiers à conserver sur la machine en SFTP
- periode : période à laquelle doit s'éxecuter le programme principal. **Il faut exécuter le fichier _automatisation_crontab.sh_ après chaque modification de la période ou du chemin du programme.**

  Arguments possibles pour le champs _période_ voir [Crontab](https://crontab.guru/):

  - @reboot
  - @yearly
  - @annually
  - @monthly
  - @weekly
  - @daily
  - @midnight
  - @hourly

- Mail :
  - email : adresse mail depuis laquelle le mail pourra être envoyé
  - key : clé ou mot de passe de l'adresse mail
  - Serveur_smtp : serveur smtp utilisé pour envoyé des mails (avec une adresse google, on utilise les serveurs smtp de google)
  - port_smtp : ports associé au serveur smtp (pour google c'est 465)
  - envoi_mail : booléen qui indique si oui ou non il faut envoyer un mail après l'éxecution du script
  - logs_mail: booléen qui indique si oui ou non on envoi en pièce jointe du mail les logs
  - Objet_mail_reussi : l'objet du mail en cas de succès du script
  - Objet_mail_echec : l'objet du mail en cas d'échec du script
  - destinataires_mail : le/les destinataire(s) du mail
- historisation : booléen qui indique si oui ou non la sauvegarde de plusieurs version sont permises.
- perdiode_suppression : en jours, indique la durée de vie des fichiers une fois qu'ils sont archivé sur la machine en sftp

<br>

## **IV - Mise en place du serveur web avec chiffrement SSL**

**Choix retenu pour le serveur : Apache2**

Mise en place du serveur Apache:

1. Installer les paquets/dépendances nécessaire en Executant en _sudo_ le fichier _depandance.sh_ sur chacune des machines.
2. Executer en _sudo_ le fichier _publish_WebServer.sh_, le fichier 'test100.sql.zip' à upload doit être dans le répertoire _/var/www/html_ de la machine qui hébergera le serveur.
3. Mettre les bon paramètres dans le fichier de configuration _configuration.json_ et le placer avec le script principal.

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
<VirtualHost *:80>
    ...
    RewriteEngine on
    RewriteCond %{HTTPS} !=on
    RewriteRule ^/?(.*) https://%{SERVER_NAME}/$1 [R=301,L]
</VirtualHost>
```

6. Relancer le serveur apache avec _sudo systemctl restart apache2_.

Le serveur web est opérationnel, on y accède avec https://[IP].

<br>

## **V - Mise en place du serveur de destination**

**Choix retenu : Protocole SFTP**
<br>
**Sur la machine qui servira de stockage :**

1. Installer OpenSSH avec la commande _sudo apt install openssh-server_
2. Créer un répertoire et ajouter son chemin dans le fichier de configuration
3. Se connecter une première fois à la machine distante en sftp depuis la machine qui exécutera le script principal en root en entrant la commande _sftp [user]@[ip]_ puis entrer le mot de passe de l'utilisateur puis autoriser la connexion. Vous êtes maintenant connecté en SFTP à la machine qui hébergera vos archives, vous pouvez fermer le terminal.

**NB :** _user_ et _ip_ ainsi que le mot de passe sont ceux de la machine distante vers laquelle on se connecte en SFTP

## **VI - Exécution du script**

Une fois toutes les étapes précedentes réalisées on peut passer à la partie éxecution du code.

1. Choisir les bons paramètres dans le fichier _configuration.json_
2. Exectuer le fichier _automatisation_crontab.sh_

**L'utilitaire est maintenant opérationnel et s'éxecutera selon la période indiqué dans _configuration.json_**

**NB 1 :** Si vous changez la période dans le fichier configuration, il faut rééxecuter _automatisation_crontab.sh_.

**NB 2 :** L'éxecution du fichier _automatisation_crontab.sh_ supprime toutes les tâches mise en place avec crontab. Si vous avez d'autres tâches à automatiser, il faut éxecuter _automatisation_crontab.sh_ en premier.
