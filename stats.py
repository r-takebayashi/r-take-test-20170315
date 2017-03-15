#!/usr/bin/env python -u
# coding: UTF-8

import sys
import subprocess
from time import sleep

args = sys.argv
argc = len(args)

if (argc == 3):
   print "測定時間: " + args[1] + "秒"
   print "テスト内容： " + args[2]


   vmstat = "vmstat 1 " + args[1] + " | awk 'BEGIN{\"hostname -s\" | getline hstnam; }; {print hstnam \"\t\" strftime(\"%y/%m/%d %H:%M:%S\") \"\t\" $0} {fflush()}' |grep -v s > `hostname -s`_vmstat_" + args[2] + "_`date \"+%Y%m%d_%H%M%S\"`.log"

   iostat = "iostat 1 " + args[1] + " -x -d | awk 'BEGIN{\"hostname -s\" | getline hstnam; }; {print hstnam \"\t\" strftime(\"%y/%m/%d %H:%M:%S\") \"\t\" $0} {fflush()}'|grep -v Device > `hostname -s`_iostat_" + args[2]+ "_`date \"+%Y%m%d_%H%M%S\"`.log"

   sar_u = "sar 1 " + args[1] + " -u -P ALL | awk 'BEGIN{\"hostname -s\" | getline hstnam; }; {print hstnam \"\t\" strftime(\"%y/%m/%d %H:%M:%S\") \"\t\" $0} {fflush()}' |grep -v \"平均値\" |grep -v Average |grep -v CPU > `hostname -s`_sar-u_" + args[2]+ "_`date \"+%Y%m%d_%H%M%S\"`.log"

   sar_q = "sar 1 " + args[1] + " -q | awk 'BEGIN{\"hostname -s\" | getline hstnam; }; {print hstnam \"\t\" strftime(\"%y/%m/%d %H:%M:%S\") \"\t\" $0} {fflush()}' | grep -v \"平均値\" |grep -v Average |grep -v ldavg > `hostname -s`_sar-q_" + args[2]+ "_`date \"+%Y%m%d_%H%M%S\"`.log"

   sar_n = "sar 1 " + args[1] + " -n DEV | awk 'BEGIN{\"hostname -s\" | getline hstnam; }; {print hstnam \"\t\" strftime(\"%y/%m/%d %H:%M:%S\") \"\t\"  $0} {fflush()}' | grep -v \"平均値\" |grep -v Average |grep -v IFACE |grep -v Linux  > `hostname -s`_sar-n_" + args[2]+ "_`date \"+%Y%m%d_%H%M%S\"`.log"

   top = "top -b -d 1 -n " + args[1] + " | awk 'BEGIN{\"hostname -s\" | getline hstnam; }; {print hstnam \"\t\" strftime(\"%y/%m/%d %H:%M:%S\") \"\t\" $0} {fflush()}'  > `hostname -s`_top_" + args[2]+ "_`date \"+%Y%m%d_%H%M%S\"`.log"



   subprocess.Popen(vmstat,shell=True)
   subprocess.Popen(iostat,shell=True)
   subprocess.Popen(sar_u,shell=True)
   subprocess.Popen(sar_q,shell=True)
   subprocess.Popen(sar_n,shell=True)
   subprocess.Popen(top,shell=True)


   if int(args[1]) != 0:
     num = int(args[1]) + 10
     sleep(num)
     print "測定が完了しました。"
   else:
     print "CTRL-Cで停止させてください。"

else:
   print "エラー：引数が足りません"
   print "コマンド例：python stats.py 10 oracle"

