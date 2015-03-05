# Pi_network-indicator
1. You need to set ACT Led to None: echo none > trigger
2. run the python with root user
    it blinks every 0.5 sec means the pi is connected to the Internet
    it flashes twice every 1 second means the pi is not connected to the Internet
3. if u wanna set the ACT led to the default function which is showing the status of your SD card: echo mmc0 > trigger

http://www.gtwang.org/2015/01/raspberry-pi-act-led-trigger.html
