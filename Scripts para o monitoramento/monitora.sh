#!/bin/bash
# $1 eh a rodada
# $2 sao os dados de conf

bash capBW.sh > mon-banda-$2-$1 &
bash capBacklog.sh > mon-backlog-$2-$1 &
bash executaMon.sh > mon-mem-$2-$1 &
sar -u 1 > mon-cpu-$2-$1 &

