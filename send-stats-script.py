#!/usr/bin/env python
# coding: UTF-8

import sys
import subprocess

cmd1 = "scp stats.py 10.44.61.11:/root/"
cmd2 = "scp stats.py 10.44.61.12:/root/"
cmd3 = "scp stats.py 10.44.61.13:/root/"
cmd4 = "scp stats.py 10.44.61.14:/root/"
cmd6 = "scp stats.py 10.44.61.16:/root/"

subprocess.call(cmd1,shell=True)
subprocess.call(cmd2,shell=True)
subprocess.call(cmd3,shell=True)
subprocess.call(cmd4,shell=True)
subprocess.call(cmd6,shell=True)

cmd11 = "ssh 10.44.61.11 \"ls -l |grep stats ; hostname\""
cmd12 = "ssh 10.44.61.12 \"ls -l |grep stats ; hostname\""
cmd13 = "ssh 10.44.61.13 \"ls -l |grep stats ; hostname\""
cmd14 = "ssh 10.44.61.14 \"ls -l |grep stats ; hostname\""
cmd16 = "ssh 10.44.61.16 \"ls -l |grep stats ; hostname\""


print
subprocess.call(cmd11,shell=True)
print
subprocess.call(cmd12,shell=True)
print
subprocess.call(cmd13,shell=True)
print
subprocess.call(cmd14,shell=True)
print
subprocess.call(cmd16,shell=True)

