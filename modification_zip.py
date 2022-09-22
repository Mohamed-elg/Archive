#!/bin/python3

from unittest import result

# import pour la comparaison de fichier sql
from difflib import Differ
from pprint import pprint

d = Differ()
result = list(d.compare(open('test100.sql', 'r').readlines(),
              open('test100-copy.sql', 'r').readlines()))
pprint(result)

v = ['voiture', 'maison']

print(v.index('voiture'))


def modification(result):
    for line in result:
        if ('+' in line):
            print("find a modification")
            return (True)
    print("no modification found")
    return (False)


modification(result)
