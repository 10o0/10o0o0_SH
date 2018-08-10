#!/bin/bash  
#测试局域网中的存活主机  
for i in {1..254}  
do  
  ping -c 1 172.17.16.$i &>/dev/null && echo 172.17.16.$i is alive &  
done  
