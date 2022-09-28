#!/bin/pyhton3

import link_sftp, json, sys

with open('configuration.json', 'r') as js:
    config = json.load(js)
    ip = config["ip_machine"]
    user = config["user_sftp"]
    mdp = config["mdp_sftp"]
js.close()

link_sftp.rm_file(ip,user, mdp, sys.argv[1])
