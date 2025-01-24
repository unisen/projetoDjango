
def get_duration_time(cookTime):
    import isodate
    #conserta a string para o formato certo
    #cookTime = cookTime.replace('PT', 'P')
    arr_duracao = []    
    duration_time = isodate.parse_duration(cookTime)
    #print(duration_time) 
    duration_str = str(duration_time)
    if 'day' in duration_str:
        
        tm = duration_str.split(', ')
        t_dias = tm[0]
        t_times = tm[1]
        ptime = tm[1].split(':')
        if 'days' in t_dias:
            t_dias = t_dias.replace('days', 'dias')
        else:
            t_dias = t_dias.replace('day', 'dia')
        
        arr_duracao.append(t_dias) 

        if int(ptime[0]) != 0:
            if int(ptime[0]) == 1:
                arr_duracao.append(str(int(ptime[0])) + ' hora')
            else:
                arr_duracao.append(str(int(ptime[0])) + ' horas')

        if int(ptime[1]) != 0:
            if int(ptime[1]) == 1:
                arr_duracao.append(str(int(ptime[1])) + ' minuto')
            else:
                arr_duracao.append(str(int(ptime[1])) + ' minutos')       

    else:

        ptime = str(duration_time).split(':')    
        if int(ptime[0]) != 0:
            if int(ptime[0]) == 1:
                arr_duracao.append(str(int(ptime[0])) + ' hora')
            else:
                arr_duracao.append(str(int(ptime[0]))+ ' horas')

        if int(ptime[1]) != 0:
            if int(ptime[1]) == 1:
                arr_duracao.append(str(int(ptime[1])) + ' minuto')
            else:
                arr_duracao.append(str(int(ptime[1])) + ' minutos')       
    
    dur_str = ' e '.join(map(str, arr_duracao))
    return dur_str




# TESTE
''' list_of_times = ['PT20M','PT50M','PT90M','PT110M','PT120M','PT180M']

for tempo in list_of_times:
    
    duracao = get_duration_time(tempo)
    print(f"Tempo: {tempo} - Conversão: {duracao}") '''