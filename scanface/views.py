from django.shortcuts import render, HttpResponse
from .models import Scanface

from deepface import DeepFace
import sqlite3
import sys
import time
import pandas as pd
import json



# Create your views here.

def hello(request):
    path = "images/"
    imagem1 = "5.png"
    imagem2 = "atual.jpg"
    
    try:
        response, pathfile = deepfacescan(path, imagem1, imagem2)
    except ValueError as e:
        print(e)
        
    key = 'Erro'
    if(key in response and response['Erro'] != ''):
        print(response)
        return HttpResponse(str(response))
       
    
    #str_con = sqlite3.connect('db.sqlite3')    
    #database_table_dict('scanface_facelogin', response, str_con)
    
    print(pathfile)
    
    
    with open(pathfile) as f:
        d = json.load(f)
        print(d)
    
    #result = '{"verified": false, "distance": 0.9028533205506547, "threshold": 0.68, "model": "VGG-Face", "detector_backend": "opencv", "similarity_metric": "cosine", "facial_areas": {"img1": {"x": 404, "y": 109, "w": 449, "h": 449, "left_eye": [696, 308], "right_eye": [563, 266]}, "img2": {"x": 164, "y": 361, "w": 840, "h": 840, "left_eye": [714, 676], "right_eye": [419, 678]}}, "time": 3.77}'
    print('----------------------------------------\n\n')
    
    #print(type(d))
    
    # Adiciona o campo files no dict
    path_files = f"{pathfile}"
    updict = {"files" : path_files}
    updict.update(d)
    
    sql = create_sql_insert(updict, 'scanface_facelogin')
    
    
    print(sql)    
    
    #sys.exit()
    
    
    try:
        insertFaceLogin(sql)
    except sqlite3.Error as error:
        print("Erro: ", error)
    #create_data(d)
    
    
    #result = '{"verified": false, "distance": 0.9028533205506547, "threshold": 0.68, "model": "VGG-Face", "detector_backend": "opencv", "similarity_metric": "cosine", "facial_areas": {"img1": {"x": 404, "y": 109, "w": 449, "h": 449, "left_eye": [696, 308], "right_eye": [563, 266]}, "img2": {"x": 164, "y": 361, "w": 840, "h": 840, "left_eye": [714, 676], "right_eye": [419, 678]}}, "time": 3.77}'
    
    #readJsonDict(str(result))
    html = str(response)
    
    #print(html)
    
    #json_dict = str(readJsonDict(d))
    #str_html = f"{html} <br> {json_dict}"
    
    #print(str_html)
    
    return HttpResponse(str(response))


def insertFaceLogin(str_sql):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = str_sql

        #sqlite_insert_query = """INSERT INTO scanface_facelogin ( `verified`, `distance`, `threshold`, `model`, `detector_backend`, `similarity_metric`, `facial_areas`, `time` ) VALUES ( "True", "0.552401273947962", "0.68", "VGG-Face", "opencv", "cosine", "{'img1': {'x': 354, 'y': 197, 'w': 224, 'h': 224, 'left_eye': [526, 285], 'right_eye': [429, 280]}, 'img2': {'x': 164, 'y': 361, 'w': 840, 'h': 840, 'left_eye': [714, 676], 'right_eye': [419, 678]}}", "3.28" )"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def database_table_dict(tabela, tbldict, str_con):
    
    # connect
    from sqlalchemy import create_engine
    #'mysql+pymysql://root:root@localhost:10076/receitasdb'
    cnx = create_engine(str_con)  
    #create json from dict
    df = pd.DataFrame.from_dict(tbldict, orient='id')
    df = df.transpose()
    #uaaau
    # CRIA A TABELA DE RECIPES DE ACORDO COM O SCHEMA DO SCRAP
    # schemna recipes
    # create table from DataFrame
    try:
        df.to_sql(tabela, cnx, if_exists='replace', index = False)
    except TypeError as errors:
        print(errors)

def readJsonDict(strdict):
    json_dict = json.loads(strdict)
    return(json_dict['facial_areas'])
    
    

def create_data(dict_data):
    # book_data = {'title': 'Biography  of Ankush Mishra', 'author': 'Ankush Mishra', 'published_date': '2024-08-16'}
    # {"verified": false, "distance": 0.7625423536893718, "threshold": 0.68, "model": "VGG-Face", "detector_backend": "opencv", "similarity_metric": "cosine", "facial_areas": {"img1": {"x": 52, "y": 125, "w": 435, "h": 435, "left_eye": [358, 300], "right_eye": [182, 300]}, "img2": {"x": 164, "y": 361, "w": 840, "h": 840, "left_eye": [714, 676], "right_eye": [419, 678]}}, "time": 3.3}
    
    book = Scanface.objects.create(**dict_data)
    book.save()
    return HttpResponse("Scanface created successfully!")


"""
Realiza a verificação facial entre duas imagens utilizando a biblioteca DeepFace.

Args:
    path (str): Caminho onde as imagens estão armazenadas
    img1 (str): Nome do arquivo da primeira imagem
    img2 (str): Nome do arquivo da segunda imagem
    
Returns:
    str: Resultado da verificação facial em formato string
"""
def deepfacescan(path, img1, img2):
    
    try:   
        result = DeepFace.verify(
            img1_path = f"{path}{img1}",
            img2_path = f"{path}{img2}"
            )
        filename = f"{img1}-{img2}" 
        pathfile = createJsonFile(filename, result)
        return result, pathfile
    
    except Exception as err:
        erro = str(err)
        erroDict = {
            "Erro": erro
            }
        filename = f"{img1}-{img2}" 
        return erroDict, filename  
        
    #json_object = json.dumps(result, indent = 4) 
    

def create_sql_insert(recipe, tabela):
    
    columns = ', '.join("`" + str(x).replace('/', '/') + "`" for x in recipe.keys())
    values = ', '.join("\"" + str(x).replace('"', '\'') + "\"" for x in recipe.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (tabela, columns, values)
    return sql


def createJsonFile(filename, result_details):
    pathfile = f"resultados/{filename}.json"
    with open(pathfile, "w") as outfile:
        json.dump(result_details, outfile)
    
    return pathfile
        

        
        
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