
cria o ambiente

python -m venv venv

ativar

.\venv\Scripts\activate

C:\Users\Notebook\AppData\Local\Programs\Python\Python38\python.exe -m venv venv

python -m pip install click

.\venv\scripts\python.exe -m pip uninstall pathlib
UPDATE pip

d:\python\python_ambient\recipes_importer-19-01-2022\venv\scripts\python.exe -m pip install --upgrade pip

.\venv\scripts\python.exe -m pip install --upgrade pip


INSTALL BIBLIOTECAS
py -m pip install django

py -m pip install requests


py -m pip install instagramy

CREATE Requirements

pip freeze > requirements.txt



INSTALL Requirements

python -m pip install -r requirements.txt


IMPORTAR DATABASE !!!!


C:\xampp\mysql\bin\mysql -u {username} -p {databasename} < file_name.sql

mysql -u root -p recipes_db < C:\importer_db\recipes_db.sql.gz

C:\Users\Tchunai\Local Sites\newchefreceitas\app\public>mysql -u root -p recipes_db < C:\importer_db\recipes_db.sql


# COMPILE Python to exe:

pyinstaller main.app.py
pyinstaller -F main.app.py
pyinstaller -F --paths=D:\Python\APP_MANAGER_IMAGES_2022\venv\Lib\site-packages main.app.py


Executar 

py sql-comidasereceitas\main_update_recipes.py
py sql-comidasereceitas\import_recipes.py 1


# ADICIONA COM FUNCAO OTIMIZADA DE INSERÇÃO DE CUSTOM FIELDS
# GANHO DE +- 20 a 30 SEGUNDOS

py sql-comidasereceitas\import_recipes_acf.py 0 1

Argumentos 
primeiro: inicio int()
segundo: contagem int()

py sql-comidasereceitas\import_recipes.py 0 3


#############################
UPDATE CUSTOM FIELDS IN ERROR import_recipes

post_id = '20420'

py sql-comidasereceitas\update_post_custom_fields.py 56456
