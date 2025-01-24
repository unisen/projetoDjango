import requests
from urllib import request
from bs4 import BeautifulSoup
import ast
import unicodedata
import re
import isodate

# ?id=20368&field=ingredients_0_ingredient_obj&value=893
def updating_custom_field(post_id, meta_key, meta_value):
	url = f"http://localhost/chefreceitas/reciper-robot/php/update_acf.php?id={post_id}&field={meta_key}&value={meta_value}"
	html_return = request.urlopen(url).read()


def import_lista_ingredientes(id):
	tabela = 'super_ingredientes_import'
	db = 'cozinhasdb'
	url = f"http://localhost/chefreceitas/reciper-robot/php/index.php?db={db}&tabela={tabela}&id={id}"
	html_return = request.urlopen(url).read()


# VERIFICA SE EXISTEM IMAGENS JA REGISTRADAS COM ESSE SLUG 
# SE SIM RETORNA UM ARRAY
def check_slug_image_for_exists(slug_post_name, qtde_imgs):
    url = f"http://localhost/chefreceitas/reciper-robot/php/checklist_imgs.php?post-name={slug_post_name}&qtde-imagens={qtde_imgs}"
    html = request.urlopen(url).read()
    x1 = html.decode()
    try:
        x1 = ast.literal_eval(x1)
        x1 = [str(n).strip() for n in x1]
        return x1
    except:
        return [False]


# VERIFICA SE A RECEITA JÁ FOI IMPORTADA!!
def check_if_recipe_imported(id_receita):
    url = f"http://localhost/chefreceitas/reciper-robot/php/check-post-exists.php?id={id_receita}"
    html = request.urlopen(url).read()
    x1 = html.decode()
    return(x1)



#https://localhost/chefreceitas/reciper-robot/php/update_cuisine.php?id=20383&slug=francesa
def updated_cuisine(post_id, cozinha_slug):
    url = f"http://localhost/chefreceitas/reciper-robot/php/update_cuisine.php?id={post_id}&slug={cozinha_slug}"
    html = request.urlopen(url).read()
    x1 = html.decode()
    return(x1)

    

# RETORNA O ID DA COZINHA ATRAVÉS DO SLUG
def get_cuisine_id_from_slug(cozinha_slug):
    url = f"http://localhost/chefreceitas/reciper-robot/php/get_cuisine_id.php?slug={cozinha_slug}"
    html = request.urlopen(url).read()
    id_cuisine = html.decode()
    return(id_cuisine)



def check_id_receita(id):        
    result_import = check_if_recipe_imported(id)
    try:
        post_id_receita = int(result_import)
    except:
        post_id_receita = result_import  

    if (isinstance(post_id_receita, int)):
        return post_id_receita
    else:
        return False


def check_is_integer(id):
	try:
		post_id_receita = int(id)
	except:
		post_id_receita = id
	if (isinstance(post_id_receita, int)):
		return post_id_receita
	else:
		return False


def get_cuisine_slug(cozinha):
    #CRIA O SLUG ATRAVES DO TITULO
    # transforma o titulo em minusculas
    x = cozinha.casefold()
    # tira os acentos se tiver
    x = str(unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore'))
    # retira os excessos da string
    x = x[2:-1]
    # troca os espaços por traços -
    slug = x.replace(" ","-")
    # printa o SLUG   
    return(slug)    


#slug = get_cuisine_slug('Australiana e Nova Zelândia')
#print(slug)
def Add_Images_Gallery(id, imgs):
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    list_imgs = ','.join([str(elem) for elem in imgs])    
    #parametro = parametro.encode("utf-8")
    base_url = f"http://localhost/chefreceitas/reciper-robot/php/insert-galeria.php?id={id}&imgs={list_imgs}"
    page = urlopen(base_url)


""" imgs = [1736, 1737, 1738, 1739]
Add_Images_Gallery(1722,imgs) """

def get_duration_time(cookTime):
    import isodate
    #conserta a string para o formato certo
    cookTime = cookTime.replace('PT', 'P')
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

