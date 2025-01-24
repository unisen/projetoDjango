from mysql.connector import Error
import mysql.connector


global host
global port
global user
global password
global database
global tabela

''' host="localhost"
port=10010
user="root"
password="root"
database="local" '''

''' host="localhost"
port=3306
user="root"
password=""
database="db_comidasereceitas"
tabela="receitas" '''

host="localhost"
port=10052
user="root"
password="root"
database="db_comidasereceitas"
tabela="receitas"

def connDB (hostvalue, porta, uservalue, passvalue, dbname):
    mydb = mysql.connector.connect(
    host=hostvalue,
    port=porta,
    user=uservalue,
    password=passvalue,
    database=dbname)
    return mydb

#insere os elementos na tabela GALLERY RECIPE
# Criada em 23/12/2021
def insert_images_gallery(tabela, id_receita, id_post, titulo_receita, path_fisico, titulo_receita_en, img_name, img_title_alt, url_download, site_da_busca):
    
    titulo_receita = titulo_receita.replace("'","''")
    titulo_receita_en = titulo_receita_en.replace("'","''")
    img_title_alt = img_title_alt.replace("'","''")
        
    
    query = "INSERT INTO %s (id_receita, id_post, titulo_receita, path_fisico, titulo_receita_en, img_name, img_title_alt, url_download, site_da_busca) VALUES (%s, %s,'%s','%s','%s','%s','%s','%s','%s')" % (tabela, id_receita, id_post, titulo_receita, path_fisico, titulo_receita_en, img_name, img_title_alt, url_download, site_da_busca)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit()
        id = mycursor.lastrowid        
        #print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        conn.close()
        return id

    except Error as error:
        print(error)



def selectAll(tabela):

    query = "SELECT * FROM " + str(tabela)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult


    except Error as error:
        print(error)


""" res = selectAll('recipes_import')
print(len(res)) """



# criada em 15 / 05 / 2021
def selectPorId(tabela, id, campos):
    
    query = "SELECT " + campos + " FROM " + str(tabela) + " WHERE id = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult

    except Error as error:
        print(error)


def selectCozinhaInterval (tabela, cozinha):
	
    option_erro = []
    option_erro.append([])
    option_erro[0].append('Opção Errada')

    first_id = f"SELECT id_receita FROM {tabela} WHERE cozinha LIKE '%{cozinha}%' ORDER BY id ASC LIMIT 1"
    last_id = f"SELECT id_receita FROM {tabela} WHERE cozinha LIKE '%{cozinha}%' ORDER BY id DESC LIMIT 1"
 
    try:
        listas = []
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        
        mycursor.execute(first_id)
        primeiro = mycursor.fetchall()

        mycursor.execute(last_id)
        ultimo = mycursor.fetchall()

        mycursor.close()
        conn.close()
        return primeiro, ultimo

    except Error as error:
        print(error)




# criada em 16 / 05 / 2021
# SELECIONA O PRIMEIRO OU O ULTIMO ID
#default first = 1 , last = 2    
def selectFirstOrLastId (tabela, opcao=1):

    option_erro = []
    option_erro.append([])
    option_erro[0].append('Opção Errada')

    if opcao == 1:
        query = "SELECT id FROM %s ORDER BY id ASC LIMIT 1" % (tabela)
    elif opcao == 2:
        query = "SELECT id FROM %s ORDER BY id DESC LIMIT 1" % (tabela)
    else:
        return option_erro
    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()
        return myresult

    except Error as error:
        print(error)

#print(selectFirstOrLastId('total_scraper',1)[0][0])

''' 
result = selectPorId(tabela,83,'id, name, description')
print(result) '''

def selectImport(tabela):
    
    query = "SELECT id, titulo, slug, featureImg, postStatus, categorias, tags, content, jsonLd FROM " + str(tabela)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult

    except Error as error:
        print(error)


def selectIds(tabela):    
    query = "SELECT id, content FROM " + str(tabela)
    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()
        return myresult

    except Error as error:
        print(error)



def selectAutorPorId(tabela, id):
    
    query = "SELECT autor_original FROM " + str(tabela) + " WHERE id = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult

    except Error as error:
        print(error)



def updateAutor(tagAutor, id):
    # <li class="sub-items">por: Ela Chris Fischman</li>     
    query = "UPDATE receitas SET autor_original = '" + str(tagAutor) + "' WHERE id = " + str(id)
    args = (tagAutor)
    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query, args)
        conn.commit()       
        print(mycursor.lastrowid, "Autor Original inserido.")
        mycursor.close()
        conn.close()
        
    except Error as error:
        conn.rollback()
        print(error)

def updateContent(tagAutor, id):
    # <li class="sub-items">por: Ela Chris Fischman</li>
    # UPDATE receitas SET content = REPLACE(content, '<li class="sub-items">por: Ela Chris Fischman</li>', '')
    # WHERE id = 7      
    query = "UPDATE receitas SET content = REPLACE(content, '" + str(tagAutor) + "','') WHERE id = " + str(id)
    #query = "UPDATE receitas SET content = '" + str(tagAutor) + "' WHERE id = " + str(id)
    
    args = (tagAutor)
    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query, args)
        conn.commit()       
        print("Update Content Success!")
        mycursor.close()
        conn.close()
        
    except Error as error:
        conn.rollback()
        print(error)


def insert_row(post_tipo, titulo, slug, featureImg, postStatus, categorias, tags, autor, descr, prepTime, servingsTipo, lista_de_ingredientes, modo_de_preparo, utensilios, content, jsonLd, datePublish, siteScrap, data_scrap):   

    query = "INSERT INTO receitas(tipopost, titulo, slug, featureImg, postStatus, categorias, tags, autor, descr, prepTime, servingsTipo, lista_de_ingredientes, modo_de_preparo, utensilios, content, jsonLd, datePublish, siteScrap, dataScrap) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
    
    args = (post_tipo, titulo, slug, featureImg, postStatus, categorias, tags, autor, descr, prepTime, servingsTipo, lista_de_ingredientes, modo_de_preparo, utensilios, content, jsonLd, datePublish, siteScrap, data_scrap)

    try:
        conn = connDB(host, port, user, password, database)

        mycursor = conn.cursor()
        mycursor.execute(query, args)
        conn.commit()        
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        conn.close()

    except Error as error:
        print(error)


# funcao insert o sql insert
def insert_json(sql):
    try:
        con = connDB(host, port, user, password, database)
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        id = cursor.lastrowid
        #print(cursor.rowcount, "record inserted.")
        cursor.close()
        con.close()
        return id
        #return cursor.rowcount
    except Error as error:
        print(error)
        #return error


#descricao = 'testaaaaando'
#sql_str = "INSERT INTO dict_schema (ldjson) VALUES ('%s')" % (descricao)
#insert_json(sql_str)



# criada em 15 / 05 / 2021
def insere_teste(campo):
       
    query = "INSERT INTO dict_schema (ldjson) VALUES ('%s')" % (campo)
 
    try:
        conn = connDB(host, port, user, password, database)

        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit()        
        print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        conn.close()

    except Error as error:
        print(error)

#insere_teste('traducao')


#insere os elementos na tabela GALLERY RECIPE
def insere_gallery_recipe(tabela, id_receita, imagens, cozinha, diretorio, slug_receita, nova_lista):
    
    query = "INSERT INTO %s (id_receita, imagens, cozinha, diretorio, slug_receita, nova_lista) VALUES (%s,'%s','%s','%s','%s','%s')" % (tabela, id_receita, imagens, cozinha, diretorio, slug_receita, str(nova_lista))

    try:
        conn = connDB(host, port, user, password, database)

        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit()        
        #print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        conn.close()

    except Error as error:
        print(error)

   
def insert_slug_gallery_import(tabela, id_receita, nome, diretorio, slug_receita):
    
    #query = f"INSERT INTO {tabela} (id_receita, nome, diretorio, slug_receita) VALUES (%s, %s,'%s','%s','%s')" % (tabela, id_receita, nome, diretorio, slug_receita)

    slug_receita = slug_receita.replace("'", "")
    slug_receita = slug_receita.replace('"','')
    nome = nome.replace("'", "")
    nome = nome.replace('"', '')


    query = f"INSERT INTO {tabela} (id_receita, nome, diretorio, slug_receita) VALUES ({id_receita}, '{nome}', '{diretorio}', '{slug_receita}')"

    try:
        conn = connDB(host, port, user, password, database)

        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit() 
        id = mycursor.lastrowid    
        #print(mycursor.rowcount, "record inserted.")
        mycursor.close()
        conn.close()
        return id       
       

    except Error as error:
        return(0)
        #print(query)
        #print(error)

# criada em 15 / 05 / 2021
def update_field(tabela, campo, novo_valor, id):
    query = "UPDATE %s SET %s = '%s' WHERE id = %s" % (tabela, campo, novo_valor, id)
    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit()       
        #print(f"Update Tabela {tabela} SET {campo} = '{novo_valor}' WHERE id = {id}")
        mycursor.close()
        conn.close()
            
    except Error as error:
        conn.rollback()
        print(error)



# criada em 15 / 05 / 2021
def update_post_id_galeria(tabela, campo, novo_valor, id):
    query = "UPDATE %s SET %s = '%s' WHERE id_receita = %s" % (tabela, campo, novo_valor, id)
    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        conn.commit()       
        #print(f"Update Tabela {tabela} SET {campo} = '{novo_valor}' WHERE id = {id}")
        mycursor.close()
        conn.close()
            
    except Error as error:
        conn.rollback()
        print(error)


#update_field('dict_schema','ldjson','foda',18)




# criada em 16 / 05 / 2021
def selectPorCampos(tabela, campos):
    
    query = "SELECT " + campos + " FROM " + str(tabela)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult

    except Error as error:
        print(error)




# criada em 16 / 05 / 2021
def selectPorCamposDict(tabela, campos):
    
    query = "SELECT " + campos + " FROM " + str(tabela)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return result

    except Error as error:
        print(error)



def selectAllDicts(tabela):

    query = "SELECT * FROM " + str(tabela)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)      

        
        desc = mycursor.description
        names = [col[0] for col in desc]
       
        data = [dict(zip(names, row)) for row in mycursor.fetchall()]
      
        mycursor.close()
        conn.close()

        return data

    except Error as error:
        print(error)




# criada em 16 / 05 / 2021
def retornaUrl(tabela, id):
    
    query = "SELECT url FROM " + tabela + " WHERE id = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult

    except Error as error:
        print(error)



def verifica_existe_id2(tabela, campo_id, id):
    query = "SELECT count(*) as existe_id FROM %s WHERE %s = %s" % (tabela, campo_id, id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()
        for r in myresult:
            res = int(list(r)[0])

        if res == 0:
            return 0
        else:
            query = "SELECT id_receita FROM %s ORDER BY %s desc LIMIT 1" % (tabela, campo_id)
            try:
                conn = connDB(host, port, user, password, database)
                mycursor = conn.cursor()
                mycursor.execute(query)
                maiorresult = mycursor.fetchall()
                mycursor.close()
                conn.close()
                for u in maiorresult:
                    ultimo = int(list(u)[0])
                return ultimo
            
            except: 
                return 'nada'



    except Error as error:
        print(error)

""" rss = verifica_existe_id('galerias_de_imagens','id_receita',83)
print(rss) """


def verifica_existe_id(tabela, campo_id, id):
    query = "SELECT count(*) as existe_id FROM %s WHERE %s = %s" % (tabela, campo_id, id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()
        for r in myresult:
          return (int(list(r)[0]))

    except Error as error:
        print(error)

#result = verifica_existe_id('images_gallery', 'id_receita', 82)
#print(result)


def get_listas_da_receita(tabela, id):
    #SELECT * FROM `osetin_recipe_ingredients` where id_receita = 83
    query = "SELECT * FROM " + str(tabela) + " WHERE id_receita = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)       
        desc = mycursor.description
        names = [col[0] for col in desc]      
        data = [dict(zip(names, row)) for row in mycursor.fetchall()]      
        mycursor.close()
        conn.close()
        return data

    except Error as error:
        print(error)




def get_lista_de_ingredientes(tabela, id):
    #SELECT * FROM `osetin_recipe_ingredients` where id_receita = 83
    query = "SELECT * FROM " + str(tabela) + " WHERE id_receita = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)       
        desc = mycursor.description
        names = [col[0] for col in desc]      
        data = [dict(zip(names, row)) for row in mycursor.fetchall()]      
        mycursor.close()
        conn.close()
        return data

    except Error as error:
        print(error)



#seleciona apenas uma receita e retorna um dicionario
def selectARecipeDict(tabela, id):
    
    query = "SELECT * FROM " + str(tabela) + " WHERE id = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)      

        
        desc = mycursor.description
        names = [col[0] for col in desc]
       
        data = [dict(zip(names, row)) for row in mycursor.fetchall()]
      
        mycursor.close()
        conn.close()

        return data

    except Error as error:
        print(error)
    

def selectARecipeDict_New(tabela, id):
	    
    query = "SELECT * FROM " + str(tabela) + " WHERE id_receita = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)      

        
        desc = mycursor.description
        names = [col[0] for col in desc]
       
        data = [dict(zip(names, row)) for row in mycursor.fetchall()]
      
        mycursor.close()
        conn.close()

        return data

    except Error as error:
        print(error)



# criada em 16 / 05 / 2021
def retornaSlug(tabela, id):
    
    query = "SELECT slug_receita FROM " + tabela + " WHERE id_receita = " + str(id)

    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult

    except Error as error:
        print(error)


""" slugss = retornaSlug('galerias_de_imagens',83)
slugs = list(slugss[0])
slug = (slugs[0])
print(slug) """


def getImagesList(id, tabela):
    query = f"SELECT nova_lista FROM {tabela} WHERE id_receita = {id}"
    try:
        conn = connDB(host, port, user, password, database)
        mycursor = conn.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        conn.close()

        return myresult

    except Error as error:
        print(error)



""" 
import re
print(getImagesList(83)[0][0])

imgs = getImagesList(83)[0][0]
print(type(imgs))
img = imgs.split('n')
print(img[0]) """