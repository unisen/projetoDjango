#pip install pandas sqlalchemy

import pandas as pd
import json
# Open JSON data
with open("resultados.json") as f:
    data = json.load(f)

# Create A DataFrame From the JSON Data
df = pd.DataFrame(data)


print 


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