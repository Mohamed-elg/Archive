#!/bin/python3

from datetime import datetime
from time import strftime


def Ecrire_rapport(msg):
    now = datetime.now()
    fichier = open("Main/logs/"+now.strftime("%Y-%m-%d")+".log", "a")
    fichier.write("\n" + now.strftime("%H:%M:%S")+"  "+msg)
    fichier.close()
