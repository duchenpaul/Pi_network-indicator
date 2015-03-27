#!/usr/bin/python
import subprocess,platform,sys
if len(sys.argv)<2:
    print "Usage: pingcheck <target>"
    sys.exit(1)
target=sys.argv[1]
if platform.system()[0]!="W":
    arg=['ping','-n',target]
    import pynotify
    notify=lambda a,b:pynotify.Notification(a,b).show()
else:
    arg=['ping','-t',target]
    import win32com.client
    axWshShell=win32com.client.Dispatch("WScript.Shell")
    notify=lambda a,b:axWshShell.Popup(b,5,a,0)
title="Ping "+target
p=subprocess.Popen(args=arg,bufsize=0,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
s=''
status=True
while p.poll()==None:
    a=p.stdout.read(1)
    if a!='\n':
        s+=a
    else:
        print s
        s=s.strip()
        if target not in s and s!='':
            if 'time=' in s and not status:
                notify(title,"Server is up!")
                status=True
            elif 'time=' not in s and status:
                notify(title,"Server is down!")
                status=False
        s=''
