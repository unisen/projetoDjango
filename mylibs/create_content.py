import json

def get_ldjson_tag(recipe_dict):
    ldjson = '<script type="application/ld+json">' + json.dumps(recipe_dict, sort_keys=True) + '</script>'
    return ldjson



def print_recipekeys(recipe_dict):
    keys = recipe_dict.keys()
    for key in keys:
        print(f"Chave: {key}")


def get_postcontent(recipe_dict):
    keys = recipe_dict.keys()
    for key in keys:
        print(f"Chave: {key}")
    

def get_modo_de_preparo(lista, chaves=['@type','text']):
    steps_list = []
    for item in lista:
        #print(f"{item[chaves[0]]} - {item[chaves[1]]}")
        steps_list.append(item[chaves[1]])
    return steps_list


def get_nivel_dificuldade(ingredientes, modo_de_preparo):
    total_linhas = len(ingredientes) + len(modo_de_preparo)
    # Nívels de Dificuldade
    # 2 - 10 fácil
    # 11 - 15 médio
    # 16 < difícil
    if total_linhas <= 10:
        return '1'
    elif total_linhas >= 11 and total_linhas <= 15:
        return '2'
    elif total_linhas >= 16:
        return '3'
    else:
        return '1'

    #print(f"{total_linhas}")
    #return total_linhas




def returnContainer(ingredientes,modo_preparo):
    #div container
    container = '<div class="receita-container">'
    lista1 = ''
    for item in ingredientes:
        #print('<li class="sub-items">' + item + '</li>')
        lista1 += '<li class="sub-items">' + item + '</li>'         
  

    lista1 = '<ul>' + lista1 + '</ul>'

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

    lista2 = '<ul>' + lista2 + '</ul>'
    #container+=descricao + '</p>' + sumario1 + '</div><hr class="divisor-sumario"><div class="row"><div class="ingredientes-receita"><h2 class="ingredientes">Ingredientes</h2>' + lista1 + '</div><div class="modo-de-preparo-receita"><h2 class="modo-de-preparo">Modo de Preparo</h2>' + lista2 + '</div></div></div>'

    # TIREI O DIV DO MOD_PREPARO
    #<div class="modo-de-preparo-receita"><h2 class="modo-de-preparo">Modo de Preparo</h2>' + lista2 + '</div>
    container+='<hr class="divisor-sumario"><br><div class="row"><div class="ingredientes-receita"><h3 class="ingredientes">Ingredientes</h3>' + lista1 + '</div><div class="modo-de-preparo-receita"><h3 class="modo-de-preparo">Modo de Preparo</h3>' + lista2 + '</div></div></div>'


    return container