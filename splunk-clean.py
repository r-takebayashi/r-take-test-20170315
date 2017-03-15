#!/usr/bin/env python
# coding: UTF-8

import sys
import subprocess

cmd1 = "/opt/splunk/bin/splunk stop -y "
cmd2 = "/opt/splunk/bin/splunk clean eventdata"
cmd3 = "/opt/splunk/bin/splunk start"

subprocess.call(cmd1,shell=True)
subprocess.call(cmd2,shell=True)
subprocess.call(cmd3,shell=True)

