#!/bin/python3

import read_configuration
import link_sftp
import sys

link_sftp.rm_file(sys.argv[1])
