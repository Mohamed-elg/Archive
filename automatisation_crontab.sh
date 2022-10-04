#!/bin/sudo bash

crontab -r
config=configuration.json
periode=$(cat $config | grep periode | sed 's/ //g' | sed 's/"periode"://g' | sed 's/"//g' | sed 's/,//g')
chemin = $(cat $config | grep chemin_Programme | sed 's/ //g' | sed 's/"chemin_Programme"://g' | sed 's/"//g' | sed 's/,//g')
echo "$periode $chemin " | crontab
