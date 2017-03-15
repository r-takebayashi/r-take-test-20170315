#!/usr/bin/env python
# coding: UTF-8

import sys
import subprocess

num = 1
while num < 7:
  if num != 5:

    cmd1 = "scp 10.44.61.1" + str(num) + ":/root/*vmstat*.log /root/logs/vmstat"
    cmd2 = "scp 10.44.61.1" + str(num) + ":/root/*iostat*.log /root/logs/iostat"
    cmd3 = "scp 10.44.61.1" + str(num) + ":/root/*sar-u*.log /root/logs/sar-u"
    cmd4 = "scp 10.44.61.1" + str(num) + ":/root/*sar-q*.log /root/logs/sar-q"
    cmd5 = "scp 10.44.61.1" + str(num) + ":/root/*sar-n*.log /root/logs/sar-n"
    cmd6 = "scp 10.44.61.1" + str(num) + ":/root/*top*.log /root/logs/top"

    subprocess.call(cmd1,shell=True)
    subprocess.call(cmd2,shell=True)
    subprocess.call(cmd3,shell=True)
    subprocess.call(cmd4,shell=True)
    subprocess.call(cmd5,shell=True)
    subprocess.call(cmd6,shell=True)


    cmd11 = "ssh 10.44.61.1" + str(num) + " \"sed -i -e 's/\\s\\+/,/g' /root/*vmstat*.log\""
    subprocess.call(cmd11,shell=True)
    cmd12 = "scp 10.44.61.1" + str(num) + ":/root/*vmstat*.log /root/splunk_logs/vmstat"
    subprocess.call(cmd12,shell=True)


    cmd21 = "ssh 10.44.61.1" + str(num) + " \"sed -i -e 's/\\s\\+/,/g' /root/*iostat*.log\""
    subprocess.call(cmd21,shell=True)
    cmd22 = "scp 10.44.61.1" + str(num) + ":/root/*iostat*.log /root/splunk_logs/iostat"
    subprocess.call(cmd22,shell=True)


    cmd31 = "ssh 10.44.61.1" + str(num) + " \"sed -i -e 's/\\s\\+/,/g' /root/*sar-u*.log\""
    subprocess.call(cmd31,shell=True)
    cmd32 = "scp 10.44.61.1" + str(num) + ":/root/*sar-u*.log /root/splunk_logs/sar-u"
    subprocess.call(cmd32,shell=True)

    
    cmd41 = "ssh 10.44.61.1" + str(num) + " \"sed -i -e 's/\\s\\+/,/g' /root/*sar-q*.log\""
    subprocess.call(cmd41,shell=True)
    cmd42 = "scp 10.44.61.1" + str(num) + ":/root/*sar-q*.log /root/splunk_logs/sar-q"
    subprocess.call(cmd42,shell=True)


    cmd51 = "ssh 10.44.61.1" + str(num) + " \"sed -i -e 's/\\s\\+/,/g' /root/*sar-n*.log\""
    subprocess.call(cmd51,shell=True)
    cmd52 = "scp 10.44.61.1" + str(num) + ":/root/*sar-n*.log /root/splunk_logs/sar-n"
    subprocess.call(cmd52,shell=True)


    cmd61 = "ssh 10.44.61.1" + str(num) + " \"sed -i -e 's/\\s\\+/,/g' /root/*top*.log\""
    subprocess.call(cmd61,shell=True)
    cmd62 = "scp 10.44.61.1" + str(num) + ":/root/*top*.log /root/splunk_logs/top"
    subprocess.call(cmd62,shell=True)

  num += 1
