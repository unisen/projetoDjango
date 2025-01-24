from django.shortcuts import render, HttpResponse
from .models import Scanface

from deepface import DeepFace
import sys
import time
import pandas as pd
import json



# Create your views here.

def hello(request):
    path = "images/"
    imagem1 = "mulher2.jpg"
    imagem2 = "atual.jpg"
    response, pathfile = deepfacescan(path, imagem1, imagem2)
    
    print(pathfile)
    
    with open(pathfile) as f:
        d = json.load(f)
        print(d)
    
    #result = '{"verified": false, "distance": 0.9028533205506547, "threshold": 0.68, "model": "VGG-Face", "detector_backend": "opencv", "similarity_metric": "cosine", "facial_areas": {"img1": {"x": 404, "y": 109, "w": 449, "h": 449, "left_eye": [696, 308], "right_eye": [563, 266]}, "img2": {"x": 164, "y": 361, "w": 840, "h": 840, "left_eye": [714, 676], "right_eye": [419, 678]}}, "time": 3.77}'
    
    sql = create_sql_insert(d, 'facelogin')
    print(sql)    
    
    #create_data(d)
    
    
    #result = '{"verified": false, "distance": 0.9028533205506547, "threshold": 0.68, "model": "VGG-Face", "detector_backend": "opencv", "similarity_metric": "cosine", "facial_areas": {"img1": {"x": 404, "y": 109, "w": 449, "h": 449, "left_eye": [696, 308], "right_eye": [563, 266]}, "img2": {"x": 164, "y": 361, "w": 840, "h": 840, "left_eye": [714, 676], "right_eye": [419, 678]}}, "time": 3.77}'
    
    #readJsonDict(str(result))
    html = str(response)
    
    #print(html)
    
    #json_dict = str(readJsonDict(d))
    #str_html = f"{html} <br> {json_dict}"
    
    #print(str_html)
    
    return HttpResponse(str(response))

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
    result = DeepFace.verify(
        img1_path = f"{path}{img1}",
        img2_path = f"{path}{img2}"
        )
    
    json_object = json.dumps(result, indent = 4) 
    filename = f"{img1}-{img2}" 
    pathfile = createJsonFile(filename, result)
    return result, pathfile

def create_sql_insert(recipe, tabela):
    columns = ', '.join("`" + str(x).replace('/', '/') + "`" for x in recipe.keys())
    values = ', '.join("\"" + str(x).replace('"', '\'') + "\"" for x in recipe.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (tabela, columns, values)
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