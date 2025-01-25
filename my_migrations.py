#pip install pandas sqlalchemy

import pandas as pd
import json
# Open JSON data
import sqlite3

with open("resultados/mulher2.jpg-adriana4.jpg.json") as f:
    data = json.load(f)

# Create A DataFrame From the JSON Data
df = pd.DataFrame(data)
print(df['similarity_metric'])

conn = sqlite3.connect('db.sqlite3')
#df = df.transpose()

df.to_sql('scanface_tblscanface', conn, if_exists='replace', index=False)

#print(df)


def database_table_dict(tabela, tbldict):     
    import sqlite3
    
    str_con = sqlite3.connect('db.sqlite3')
    
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