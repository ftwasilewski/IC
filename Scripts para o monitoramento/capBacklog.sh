#!/bin/sh
#Primeiro argumento eh o periodo
#segundo argumento eh o arquivo saida

while [ 1 ] 
do 
	tc -s -d qdisc | grep backlog
	sleep 1
done 
