#!/bin/sudo bash

p=configuration.json
x=$(cat $p | grep periode | sed 's/ //g' | sed 's/"periode"://g' | sed 's/"//g' | sed 's/,//g')
echo "@$x /home/mohamed/Bureau/SFTP/test.txt" | crontab
