#!/usr/bin/env python
# coding: UTF-8

import sys
import subprocess

cmd1 = "rm -f /root/logs/*/*"
cmd2 = "rm -f /root/splunk_logs/*/*"

subprocess.call(cmd1,shell=True)
subprocess.call(cmd2,shell=True)
