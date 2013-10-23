# argv[1] eh o nome do programa (bt, cg, ep, ft, is, lu, mg, sp)

from subprocess import call
import sys

if len(sys.argv) == 2:
	call(["python", "make-data-banda.py", sys.argv[1]])
	call(["python", "make-data-cpu.py", sys.argv[1]])
else :
	print "Informe o programa no momento da execucao, ex: python make-charts.py bt"
