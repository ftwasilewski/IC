import sys
from subprocess import call

#c_peak = 95.0 				Desnecessario
#c_peakThreshold = 30.0		Desnecessario
c_underLimit = 80.0
c_upperLimit = 100.0

r_peak = 95.0
r_peakThreshold = 30.0
r_underLimit = 50.0
r_upperLimit = 80.0

#l_peak = 95.0				Desnecessario
#l_peakThreshold = 30.0		Desnecessario
l_underLimit = 0.0
l_upperLimit = 50.0

N = 1800 # Tamanho da amostra (segundos)
output_file_name = "data-cpu-" + str(N) + ".dat"

mon_cpu_file = open('mon-cpu-' + sys.argv[1],'r')
output_file  = open(output_file_name, 'w')
estatistica_file  = open('estatistica-' + sys.argv[1], 'a')

original = mon_cpu_file.readlines()

output_file.write("#" + original[0])
output_file.write("#" + original[1])
output_file.write("#" + original[2])

#num_window = int(N/360) # Numero de "janelas" que serao analisadas
um = 0.0 # Media de uso de cpu (100% - %idle)
sm = 0.0 # Media de steal da cpu
npeak = 0 # Numero de vezes que o consumo foi superior ao peak

for i in range (1,N+1):
	um += 100.00 - float(original[i + 2][-7:])
	sm += float(original[i + 2][-17:-11])
	if 100.00 - float(original[i + 2][-7:]) > r_peak :
		npeak += 1
	output_file.write(str(i) + ' ' + original[i + 2])

mon_cpu_file.close()
output_file.close()

# Geracao da estatistica
um = um / N
sm = sm / N
print >> estatistica_file, "#################"
print >> estatistica_file, "CPU"
print >> estatistica_file, "n =", N
print >> estatistica_file, "um =", um
print >> estatistica_file, "sm =", sm

# regularUsage
if um < r_underLimit :
	print >> estatistica_file, "utilizacao = regular" # Adicionar outras sentencas
elif um < r_upperLimit :
	print >> estatistica_file, "utilizacao = regular"
else :
	print >> estatistica_file, "utilizacao = critical"

# Geracao do grafico 640x480
arquivo_temp = open('temp3.gp', 'w')
temp3 = """
#!/usr/bin/gnuplot
reset
set terminal png size 640,480
set xlabel \"Tempo (segundos)\"
set ylabel \"Uso de CPU (%)\"
set grid
unset key
set output \"grafico-cpu-640x480.png\"
plot \"data-cpu-1800.dat\" using ($1):(100-$9)
"""
arquivo_temp.write(temp3)
arquivo_temp.close()

# Geracao do grafico 1280x480
arquivo_temp = open('temp4.gp', 'w')
temp4 = """
#!/usr/bin/gnuplot
reset
set terminal png size 1280,480
set xlabel \"Tempo (segundos)\"
set ylabel \"Uso de CPU (%)\"
set grid
unset key
set output \"grafico-cpu-1280x480.png\"
plot \"data-cpu-1800.dat\" using ($1):(100-$9)
"""
arquivo_temp.write(temp4)
arquivo_temp.close()

call(["gnuplot", "temp3.gp"])
call(["gnuplot", "temp4.gp"])
call(["rm", "temp3.gp"])
call(["rm", "temp4.gp"])
call(["rm", output_file_name])
