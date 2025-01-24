

def receitaContainer(titulo,descricao,preptime,cooktime,totaltime,servings,ingredientes,modo_preparo):
    #div container
    print('<div class="receita-container">')
    #div sumario
    print('<div class="sumario-receita">')
    print('<p class="description-receita">')
    descricao = f"Receita de <strong>{titulo}</strong>, aprenda a preparar com Chef Receitas, receitas para todos os momentos, gostos e sabores.<br>" + descricao
    print(descricao)
    print('</p>')
    sumario1 = """<div class="nivel"><span class="label">Nível:</span>
                        <p></p>
                        <p>Expert</p>
                    </div>
                    <div class="tempo-de-preparo"><span class="label">Tempo de Preparo:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                     <div class="tempo-de-cozimento"><span class="label">Tempo de Cozimento:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                     <div class="tempo-de-total"><span class="label">Tempo de Total:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                    <div class="rendimento"><span class="label">Rendimento:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                """ % (preptime,cooktime,totaltime,servings)
    
    print(sumario1)

    print('</div>')
    print('<hr class="divisor-sumario"><div class="row">')

    #ingredientes loop
    print('<div class="ingredientes-receita"><h2 class="ingredientes">Ingredientes</h2>')
    """  <p class="subtitulos-receita">CARNE-SECA</p> """
    for item in ingredientes:
        print('<li class="sub-items">' + item + '</li>')         
    print('</div>')

    #modo de preparo loop
    print('<div class="modo-de-preparo-receita"><h2 class="modo-de-preparo">Modo de Preparo</h2>')
    """ <p class="subtitulos-receita">CARNE-SECA</p> """
    i=1
    for item in modo_preparo:
        print('<li class="sub-items">'+str(i)+') ' + item + '</li>')
        i+=1

    print('</div></div></div>')



    

def returnContainer(titulo,descricao,preptime,cooktime,totaltime,servings,ingredientes,modo_preparo):
    #div container
    container = '<div class="receita-container"><div class="sumario-receita"><p class="description-receita">'
    descricao = f"Receita de <strong>{titulo}</strong>, aprenda a preparar com Chef Receitas, receitas para todos os momentos, gostos e sabores.<br>" + descricao
    
    sumario1 = """<div class="tempo-de-preparo"><span class="label"><i class="os-icon os-icon-thin-clock-busy"></i> Preparo:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                     <div class="tempo-de-cozimento"><span class="label"><i class="os-icon os-icon-thin-clock-busy"></i> Cozimento:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                     <div class="tempo-de-total"><span class="label"><i class="os-icon os-icon-thin-clock-busy"></i> Tempo Total:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div> 
                    <div class="rendimento"><span class="label"><i class="os-icon os-icon-thin-paper-holes-text"></i> Rendimento:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                """ % (preptime,cooktime,totaltime,servings)
    
    lista1 = ''
    for item in ingredientes:
        #print('<li class="sub-items">' + item + '</li>')
        lista1 += '<li class="sub-items">' + item + '</li>'         
  

    i=1
    lista_steps_preparo = []

    lista2 = ''
    for item in modo_preparo:
        #print('<li class="sub-items">'+str(i)+') ' + item + '</li>')
        lista2+='<li class="sub-items">'+str(i)+') ' + item + '</li>'
        
        #step_preparo = str(i)+') '+item
        step_preparo = item
        lista_steps_preparo.append(step_preparo)
        i+=1

    #container+=descricao + '</p>' + sumario1 + '</div><hr class="divisor-sumario"><div class="row"><div class="ingredientes-receita"><h2 class="ingredientes">Ingredientes</h2>' + lista1 + '</div><div class="modo-de-preparo-receita"><h2 class="modo-de-preparo">Modo de Preparo</h2>' + lista2 + '</div></div></div>'

    # TIREI O DIV DO MOD_PREPARO
    #<div class="modo-de-preparo-receita"><h2 class="modo-de-preparo">Modo de Preparo</h2>' + lista2 + '</div>
    container+=descricao + '</p>' + sumario1 + '</div><hr class="divisor-sumario"><div class="row"><div class="ingredientes-receita"><h2 class="ingredientes">Ingredientes</h2>' + lista1 + '</div></div></div>'


    return container, lista_steps_preparo



      

def returnContainerAntigo(titulo,descricao,preptime,cooktime,totaltime,servings,ingredientes,modo_preparo):
    #div container
    container = '<div class="receita-container"><div class="sumario-receita"><p class="description-receita">'
    descricao = f"Receita de <strong>{titulo}</strong>, aprenda a preparar com Chef Receitas, receitas para todos os momentos, gostos e sabores.<br>" + descricao
    
    sumario1 = """<div class="nivel"><span class="label">Nível:</span>
                        <p></p>
                        <p>Expert</p>
                    </div>
                    <div class="tempo-de-preparo"><span class="label">Tempo de Preparo:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                     <div class="tempo-de-cozimento"><span class="label">Tempo de Cozimento:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                     <div class="tempo-de-total"><span class="label">Tempo de Total:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                    <div class="rendimento"><span class="label">Rendimento:</span>
                        <p></p>
                        <li class="sub-items"> %s </li>
                    </div>
                """ % (preptime,cooktime,totaltime,servings)
    
    lista1 = ''
    for item in ingredientes:
        #print('<li class="sub-items">' + item + '</li>')
        lista1 += '<li class="sub-items">' + item + '</li>'         
  

    i=1
    lista_steps_preparo = []

    lista2 = ''
    for item in modo_preparo:
        #print('<li class="sub-items">'+str(i)+') ' + item + '</li>')
        lista2+='<li class="sub-items">'+str(i)+') ' + item + '</li>'
        
        #step_preparo = str(i)+') '+item
        step_preparo = item
        lista_steps_preparo.append(step_preparo)
        i+=1

    #container+=descricao + '</p>' + sumario1 + '</div><hr class="divisor-sumario"><div class="row"><div class="ingredientes-receita"><h2 class="ingredientes">Ingredientes</h2>' + lista1 + '</div><div class="modo-de-preparo-receita"><h2 class="modo-de-preparo">Modo de Preparo</h2>' + lista2 + '</div></div></div>'

    # TIREI O DIV DO MOD_PREPARO
    #<div class="modo-de-preparo-receita"><h2 class="modo-de-preparo">Modo de Preparo</h2>' + lista2 + '</div>
    container+=descricao + '</p>' + sumario1 + '</div><hr class="divisor-sumario"><div class="row"><div class="ingredientes-receita"><h2 class="ingredientes">Ingredientes</h2>' + lista1 + '</div></div></div>'


    return container, lista_steps_preparo


