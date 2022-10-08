#!/bin/bash

p=configuration.json
x=$(cat $p | grep url_fichier | sed 's/ //g' | sed 's/"url_fichier"://g' | sed 's/"//g' | sed 's/,//g')
#changer le nom du fichier
file='test100.sql.zip'

wget $x --no-check-certificate
unzip $file
rm $file
