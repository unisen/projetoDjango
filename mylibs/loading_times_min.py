####################################################################
# 
# 
# 	MODULO DE CONTROLE DO TEMPO DE PROCESSAMENTO, DO CODIGO, FUNCAO, ETC
# 	Uso:  tempo_inicial = show_tempo_total()   => retorna o tempo inicial
# 		  show_tempo_total(tempo_inicial)	   => printa o tempo final já formatado
# #
def show_tempo_total(start_time=0):
	import time
	import math
	import numpy

	if (start_time==0):
		init_time = time.time()
		return init_time
		
	tempo = (time.time() - start_time)

	if tempo < 60:

		tsegundos = time.time() - start_time
		segundos = math.floor(tsegundos)
		a = tsegundos
		b = a - numpy.fix(a)
		milesimos = b * 1000
		if segundos > 1:
			plural = 's'
		else:
			plural = ''

		timeDuration = "%s segundo%s e %s milisegundos" % (str(segundos),plural,str(math.floor(milesimos)))
		 
	
		#segundos = ("%.2f" % segundos)
		#timeDuration = " %s seconds -" % (segundos)
	else:
		tminutos = (time.time() - start_time)
		tminutos = tminutos / 60

		if tminutos < 60:            
			minutos = math.floor(tminutos)
			a = tminutos
			b = a - numpy.fix(a)
			segundos = b * 60

			#tminutos = ("%.2f" % tminutos)
			#timeDuration = " %s minutos -" % str(tminutos)
			timeDuration = "%s minutos e %s segundos" % (str(minutos),str(math.floor(segundos)))
			


		else:
			a = thoras = tminutos / 60
			horas = math.floor(thoras)
			b = a - numpy.fix(a)
			minutos = b * 60
			
			thoras = ("%.2f" % thoras)
			timeDuration = "%s horas e %s minutos" % (str(horas),str(math.floor(minutos)))

			
	#print(timeDuration)
	return(timeDuration)