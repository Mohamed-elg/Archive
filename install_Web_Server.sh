#!/bin/sudo bash

#Fichier à exécuter uniquement s'il n'y a pas de serveur web sur une distribution basé Debian

echo "nom du fichier à upload ? /chemin/nom.extension"
read nom
sudo apt update
sudo apt install apache2 openssl

code="<!DOCTYPE><html><head><meta http-equiv='Content-Type' content='text/html charset=UTF-8'/><title>Upload</title></head><body><a href=$nom>$nom</a></body></html>"

sudo echo $code >index.html
sudo systemctl restart apache2
#Si tout s'est bien passé, le serveur web est fonctionnel

#Mise en place du SSL
sudo echo "Mise en place du SSL"
sleep 2

$conf="<Directory /var/www/html>
 AllowOverride ALL
</Directory>"

sudo mkdir /etc/apache2/certs
sudo openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out apache.crt -keyout apache.key
sudo mv apache.crt /etc/apache2/certs
sudo mv apache.key /etc/apache2/certs

sudo echo $conf >>/etc/apache2/apache2.conf

config_file='
<VirtualHost *:443>
 ServerAdmin webmaster@localhost
 DocumentRoot /var/www/html
 ErrorLog ${APACHE_LOG_DIR}/error.log
 CustomLog ${APACHE_LOG_DIR}/access.log combined
 SSLEngine on
 SSLCertificateFile /etc/apache2/certs/apache.crt
 SSLCertificateKeyFile /etc/apache2/certs/apache.key
</VirtualHost>
'

sudo echo $config_file >>/etc/apache2/sites-enabled/000-default.conf

sudo systemctl restart apache2
