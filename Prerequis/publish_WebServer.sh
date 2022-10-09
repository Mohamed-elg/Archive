#!/bin/sudo bash

#Fichier à exécuter uniquement s'il n'y a pas de serveur web sur une distribution basé Debian
nom='test100.sql.zip'
code="<!DOCTYPE><html><head><meta http-equiv='Content-Type' content='text/html charset=UTF-8'/><title>Upload</title></head><body><a href=$nom>$nom</a></body></html>"

sudo echo $code >/var/www/html/index.html
sudo systemctl restart apache2
echo "Le serveur web est opérationnel"
#Si tout s'est bien passé, le serveur web est fonctionnel
