#!/usr/bin/env python
# coding: UTF-8

import sys
import subprocess
from time import sleep

cmd1 = "pssh -h hosts.txt -t 100000000 -i \"python stats.py 3600 log_collect_test\""
cmd2 = "python get-logs.py"
cmd3 = "python remove-logs.py"

print "ログを取得します" 
subprocess.call(cmd1,shell=True)
print "完了しました"
sleep(10)
print "ログを収集します"
subprocess.call(cmd2,shell=True)
print "完了しました"
sleep(10)
print "ログを削除します"
subprocess.call(cmd3,shell=True)
print "完了しました"


