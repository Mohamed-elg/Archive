#!/bin/python3

import read_configuration
import link_sftp
import sys

link_sftp.rm_file(read_configuration.ip, read_configuration.user,
                  read_configuraion.mdp, sys.argv[1])
