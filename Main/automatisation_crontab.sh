#!/bin/sudo bash

crontab -r
config=configuration.json
periode=$(cat $config | grep -m 1 "periode" | sed 's/ //g' | sed 's/"periode"://g' | sed 's/"//g' | sed 's/,//g')
chemin=$(cat $config | grep "chemin_Programme" | sed 's/ //g' | sed 's/"chemin_Programme"://g' | sed 's/,//g' | sed 's/"//g')
echo "$periode cd $chemin && python3 main.py" | crontab
echo "Tâche automatisé"
