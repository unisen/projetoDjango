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
database="local"
tabela="receitas" '''

host="localhost"
port=3306
user="root"
password=""
database="wp_chefblog"
tabela="receitas"


def connDB (hostvalue, porta, uservalue, passvalue, dbname):
    mydb = mysql.connector.connect(
    host=hostvalue,
    port=porta,
    user=uservalue,
    password=passvalue,
    database=dbname)
    return mydb

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



def selectPorId(tabela, id):
    
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

