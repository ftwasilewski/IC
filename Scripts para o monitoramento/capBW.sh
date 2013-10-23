#!/bin/sh

#n=1
x1=`awk '/eth0/ {gsub(":", " "); print $10}' </proc/net/dev` 
#x1=`awk '/eth0/ {print $9}' </proc/net/dev` 
#x1=`grep eth0 /proc/net/dev | cut -f2- -d":" | cut -f9 -d" "`
while [ 1 ]
do
	sleep 1
	#( echo $n: ; cat /proc/net/dev ; echo "=================" )>>/tmp/procnetdev 
	#n=`expr $n + 1`
	x2=`awk '/eth0/ {gsub(":", " "); print $10}' </proc/net/dev` 
        x3=`expr $x2 - $x1`
	x3=`expr $x3 / 1024` 
	echo $x3 
	x1=$x2
done
