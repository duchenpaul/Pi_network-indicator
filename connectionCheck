#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Author:Skate
import os,sys,re
import subprocess

def NetCheck(ip):
   try:
    p = subprocess.Popen(["ping -c 1 -w 1 "+ ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    out=p.stdout.read()
    #err=p.stderr.read()
    regex=re.compile('100% packet loss')
    #print out
    #print regex
    #print err
    if len(regex.findall(out)) == 0:
        print ip + ': host up'
        return 'UP'
    else:
        print ip + ': host down'
        return 'DOWN'
   except:
    print 'NetCheck work error!'
    return 'ERR'
if __name__ == '__main__':
    NetCheck('10.20.0.56')
    NetCheck('10.10.0.56')
    NetCheck('10.10.0')
   
