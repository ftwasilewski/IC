import sys
from subprocess import call
from math import sqrt

N = 1800 # Tamanho da amostra (segundos)
output_file_name = "data-banda-" + str(N) + ".dat"

mon_banda_file = open('mon-banda-' + sys.argv[1],'r')
mon_backlog_file = open('mon-backlog-' + sys.argv[1],'r')

output_file = open(output_file_name, 'w')
estatistica_file  = open('estatistica-' + sys.argv[1], 'w')

mon_banda = mon_banda_file.readlines()
mon_backlog = mon_backlog_file.readlines()

# Variaveis para o calculo do coeficiente de variacao
soma2 = 0
media = 0.0
aux = 0.0
s = 0.0  # Variancia
d = 0.0  # Desvio padrao (raiz(s))
cv = 0.0 # Coeficiente de variacao
requeue = 0

for i in range (1,N+1):
	aux = int(mon_banda[i - 1])
	soma2 += aux*aux
	media += aux
	output_file.write(str(i) + ' ' + mon_banda[i - 1])

mon_banda_file.close()
output_file.close()

# Geracao da estatistica
media = media/N
s = (soma2 - N*(media*media)) / (N-1)
d = sqrt(s)
cv = (d/media) * 100
requeue = int(mon_backlog[N][mon_backlog[N].find('s')-len(mon_backlog[N])+1:]) - int(mon_backlog[0][mon_backlog[0].find('s')-len(mon_backlog[0])+1:])
print >> estatistica_file, "#################"
print >> estatistica_file, "REDE"
print >> estatistica_file, "n =", N
print >> estatistica_file, "media =", media
print >> estatistica_file, "s =", s
print >> estatistica_file, "d =",  d
print >> estatistica_file, "cv (%) =", cv
print >> estatistica_file, "requeues =", requeue

if cv > 5 and requeue == 0 :
	print >> estatistica_file, "utilizacao = low"
elif cv <= 5 and requeue == 0 :
	print >> estatistica_file, "utilizacao = regular"
elif cv <= 5 and requeue > 0 :
	print >> estatistica_file, "utilizacao = critical"

estatistica_file.close()
mon_backlog_file.close()

# Geracao do grafico 640x480
arquivo_temp = open('temp1.gp', 'w')
temp1 = """
#!/usr/bin/gnuplot
reset
set terminal png size 640,480
set xlabel \"Tempo (segundos)\"
set ylabel \"Consumo de Banda (KB)\"
set grid
unset key
set output \"grafico-banda-640x480.png\"
plot \"data-banda-1800.dat\"
"""
arquivo_temp.write(temp1)
arquivo_temp.close()

# Geracao do grafico 1280x480
arquivo_temp = open('temp2.gp', 'w')
temp2 = """
#!/usr/bin/gnuplot
reset
set terminal png size 1280,480
set xlabel \"Tempo (segundos)\"
set ylabel \"Consumo de Banda (KB)\"
set grid
unset key
set output \"grafico-banda-1280x480.png\"
plot \"data-banda-1800.dat\"
"""
arquivo_temp.write(temp2)
arquivo_temp.close()

call(["gnuplot", "temp1.gp"])
call(["gnuplot", "temp2.gp"])
call(["rm", "temp1.gp"])
call(["rm", "temp2.gp"])
call(["rm", output_file_name])
