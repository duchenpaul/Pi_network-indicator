import smtplib, string, subprocess
import time, urllib

def blink(y,n,t):
  tmp = 0
  while (tmp < t):
    #subprocess.Popen(['echo 1 > /sys/devices/platform/leds-gpio/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    subprocess.Popen(['echo 1 > /sys/class/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    # print("11111")
    time.sleep(y)
    #subprocess.Popen(['echo 0 > /sys/devices/platform/leds-gpio/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    subprocess.Popen(['echo 0 > /sys/class/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    # print("00000")
    time.sleep(n)
    tmp += y+n

  #subprocess.Popen(['echo 0 > /sys/devices/platform/leds-gpio/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
  subprocess.Popen(['echo 0 > /sys/class/leds/led0/brightness'], stdout=subprocess.PIPE, shell=True).communicate()[0]
  # print("------")

def pulse_blink(t):
  tmp = 0
  # print "t= %d" %(t)
  while (tmp < t):
    # print(tmp)
    blink(.1,.1,.4)
    time.sleep(.5)
    tmp += 1
    pass
  pass

def check_network_with_blink():
    flag = -1
    while True:
        try:
            result=urllib.urlopen('http://baidu.com').read()
            print result
            print "Network is Ready!"
            print "flag= %d" %(flag)
            blink(.5,.5,5)

            if flag == 0: #send a mail when internet reconnects
              print "=========Network reconnected!=========="
              send_mail()
              flag = 1
              pass

            break
        except Exception , e:
           print e
           print "Network is not ready,Sleep 5s...."
           flag = 0
           print "flag= %d" %(flag)
           pulse_blink(5)
    return True

def send_mail():
    # Settings
    fromaddr = 'qq859755014@126.com'
    toaddr = 'qq859755014@126.com'

    # Googlemail login details
    username = 'qq859755014@126.com'
    password = '1qazxsw2'

    output_date = subprocess.Popen(['date |cut -d " " -f 2-10| sed \'s/ CST.*//g\''], stdout=subprocess.PIPE, shell=True).communicate()[0]
    output_temp = subprocess.Popen(['/opt/vc/bin/vcgencmd measure_temp | cut -b 6-11'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    output_ip = subprocess.Popen(['curl -o - http://www.cpanel.net/showip.cgi'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    output_ESSID = subprocess.Popen(['iwconfig wlan0|grep ESSID|cut -d " " -f 9|sed \'s/ESSID:"//g\'|sed \'s/"//g\''], stdout=subprocess.PIPE, shell=True).communicate()[0]
    output_inner_ip = subprocess.Popen(['echo $(hostname -I) || true'], stdout=subprocess.PIPE, shell=True).communicate()[0]
    
    send_date = "Boot time: %s" % (output_date)
    send_temp = "Temperature: %s" % (output_temp)
    send_ip = "External IP: %s" % (output_ip)
    send_ESSID = "ESSID: %s" % (output_ESSID)
    send_inner_ip = "LAN IP: %s" % (output_inner_ip)

    BODY = string.join((
    "From: %s" % fromaddr,
    "To: %s" % toaddr,
    "Subject: Your RasPi just reconnected to the Internet @ %s" % (output_date),
    "",
    send_date,
    send_temp,
    send_ip,
    send_inner_ip,
    send_ESSID,
    ), "\r\n")




    # send the email
    server = smtplib.SMTP('smtp.126.com')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddr, BODY)
    server.quit()
pass

subprocess.Popen(['echo none > /sys/class/leds/led0/trigger'], stdout=subprocess.PIPE, shell=True).communicate()[0]
while True:
  check_network_with_blink()
pass
