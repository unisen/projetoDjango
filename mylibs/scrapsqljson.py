import scrape_schema_recipe
import pymysql
import pandas as pd
from pandas import errors

from mysql.connector import Error
import mysql.connector

global host
global port
global user
global password
global database
global tabela
global str_con


host="localhost"
port=3306
user="root"
password=""
database="db_comidasereceitas"

#tabela="teste_schema"

str_con = 'mysql+pymysql://'+user+':'+password+'@'+host+':'+str(port)+'/'+database

def get_str_conn(host="localhost",port=10076,user="root",password="root",database="scraper2021"):
    
    #tabela="teste_schema"
    str_con = 'mysql+pymysql://'+user+':'+password+'@'+host+':'+str(port)+'/'+database
    return str_con


#retorna a conexao
def connDB (hostvalue, porta, uservalue, passvalue, dbname):
    myconn = mysql.connector.connect(
    host=hostvalue,
    port=porta,
    user=uservalue,
    password=passvalue,
    database=dbname)
    return myconn

#retorna a conexao
def conectsql(host,user,password,db):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 db=db)
    return connection


# recipe as dict , tabela = nome da tabela ja criada no banco de dados
def create_sql_insert(recipe, tabela):
    columns = ', '.join("`" + str(x).replace('/', '/') + "`" for x in recipe.keys())
    values = ', '.join("\"" + str(x).replace('"', '\'') + "\"" for x in recipe.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (tabela, columns, values)
    return sql


# ex: url = 'https://www.allrecipes.com/recipe/255989/spicy-chicken-and-hominy-mexican-soup/'
# retorna o ld+json da pagina em formato de dicionario (dict)
def recipe_dict(url):
    #url = 'https://www.allrecipes.com/recipe/255989/spicy-chicken-and-hominy-mexican-soup/'
    try:
        recipe_list = scrape_schema_recipe.scrape_url(url, python_objects=False)
        recipe = recipe_list[0]
        return recipe #dict
    
    except:
        #recipe_list = scrape_schema_recipe.scrape_url(url, python_objects=False)
        #recipe = recipe_list[0]
        # Se der Erro retorna 0
        return 0 #recipe empty Error


# funcao insert o sql insert
def insert_json(sql):

    while True:
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
            insert_json(sql)
            #insert_json(sql)
                #return error


def database_table_dict(tabela, tbldict, str_con):     
    # connect
    from sqlalchemy import create_engine
    #'mysql+pymysql://root:root@localhost:10076/receitasdb'
    cnx = create_engine(str_con)  
    #create json from dict
    df = pd.DataFrame.from_dict(tbldict, orient='index')
    df = df.transpose()
    #uaaau
    # CRIA A TABELA DE RECIPES DE ACORDO COM O SCHEMA DO SCRAP
    # schemna recipes
    # create table from DataFrame
    try:
        df.to_sql(tabela, cnx, if_exists='replace', index = False)
    except TypeError as errors:
        print(errors)


def manage_database(recipe_dict, tabela,str_con=str_con):     
    # connect
    from sqlalchemy import create_engine
    #'mysql+pymysql://root:root@localhost:10076/receitasdb'
    cnx = create_engine(str_con)  
    #create json from dict
    df = pd.DataFrame.from_dict(recipe_dict, orient='index')
    df = df.transpose()
    #uaaau
    # CRIA A TABELA DE RECIPES DE ACORDO COM O SCHEMA DO SCRAP
    # schemna recipes
    # create table from DataFrame
    try:
        df.to_sql(tabela, cnx, if_exists='replace', index = False)
    except TypeError as errors:
        print(errors)


''' url = 'https://www.allrecipes.com/recipe/246118/agua-fresca-de-pepino-cucumber-limeade/'
#url = 'https://www.allrecipes.com/recipe/255989/spicy-chicken-and-hominy-mexican-soup/'
print(recipe_dict(url)) '''        

#url = 'https://www.allrecipes.com/recipe/255989/spicy-chicken-and-hominy-mexican-soup/'
#url = 'https://www.allrecipes.com/recipe/246332/carnitas-pressure-cooker/'
#url = 'https://www.allrecipes.com/recipe/260611/gluten-free-corn-tortillas-with-3-ingredients/'

#recipe = recipe_dict(url)
#manage_database(str_con,recipe,tabela)

#sql = create_sql_insert(recipe, tabela)
#print(sql)
#sql = "INSERT INTO `teste` (`nome`) VALUES ('Diego')"
#insert_json(sql)

