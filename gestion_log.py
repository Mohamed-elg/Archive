#!/bin/python3

import os
from datetime import datetime
from time import strftime


def creer_rapport():
    now = datetime.now()
    os.system("touch logs/"+now.strftime("%Y-%m-%d")+".txt")


def Ecrire_rapport(msg):
    now = datetime.now()
    fichier = open("logs/"+now.strftime("%Y-%m-%d")+".txt", "a")
    fichier.write("\n" + now.strftime("%H:%M:%S")+"  "+msg)
    fichier.close()
