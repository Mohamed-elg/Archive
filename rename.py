#!/bin/python3

import os
from datetime import datetime

nom = 'test.txt'
extension = '.txt'

stat = os.stat(nom)
creation_date = str(datetime.fromtimestamp(stat.st_mtime))[0:10]
os.rename(nom, creation_date+extension)
