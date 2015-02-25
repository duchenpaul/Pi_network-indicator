#!/bin/bash
# check host alive
# edit by www.ahlinux.com
# At 2013-7-22
#declare var

GATEWAY=`cat /etc/sysconfig/network-scripts/ifcfg-eth0 | grep 'GATEWAY=' | sed 's/^.*GATEWAY=//g'`
NAMESERVER=`cat /etc/resolv.conf | grep 'nameserver ' | sed 's/^.*nameserver //g'`
ping -c 5 127.0.0.1
if [ "$?" != "0" ]; then
   echo "the interface error"
fi
ping -c 5 $GATEWAY
if [ "$?" != "0" ]; then
   echo "the gateway is unreachable"
fi
ping -c 5 $NAMESERVER
if [ "$?" != "0" ]; then
   echo "the remote host is down"
fi
exit 0

# 代码说明：
# 1，GATEWAY=`cat /etc/sysconfig/network-scripts/ifcfg-eth0 | grep 'GATEWAY=' | sed 's/^.*GATEWAY=//g'`
# 获取网关信息。
# 2，NAMESERVER=`cat /etc/resolv.conf | grep 'nameserver ' | sed 's/^.*nameserver //g'`
# 获取dns信息。
# 3，以上代码检测5次本地回环地址127.0.0.1。
# 检测5次网关是否连通。
# 检测5次dns是否申通。
# 分别给出检测结果提示。
