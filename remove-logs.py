#!/usr/bin/env python
# coding: UTF-8

import sys
import subprocess

print "ログを削除します"

cmd11 = "ssh 10.44.61.11 \"rm -f *.log\""
cmd12 = "ssh 10.44.61.12 \"rm -f *.log\""
cmd13 = "ssh 10.44.61.13 \"rm -f *.log\""
cmd14 = "ssh 10.44.61.14 \"rm -f *.log\""
cmd16 = "ssh 10.44.61.16 \"rm -f *.log\""


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


