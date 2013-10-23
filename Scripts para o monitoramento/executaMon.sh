#!/bin/sh

echo 'MemTotal	MemFree	Buffers	Cached	Slab	Comm_AS	RES'
while [ 1 ] #for ((i=1;i<=$1;i++))
do 
	egrep '^(MemTotal|MemFree|Buffers|Cached|Slab|Committed)' < /proc/meminfo | awk {'print $2;'} |tr "\n" "\t" 
	egrep '^(MemTotal|MemFree|Buffers|Cached|Slab|Committed)' < /proc/meminfo | awk {'print $2;'} |tr "\n" "\t" | awk {'$MEM=$1-($2+$3+$4+$5); print $MEM;'} 
	sleep 1
done 
