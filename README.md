Django

django-admin startproject main .

python manage.py migrate
python manage.py createsuperuser

python manage.py startapp scanface

Finally, run python manage.py loaddata <json filepath>. And you're done!



To dump data:
python manage.py dumpdata app.model_name --indent 4 > fixtures/model_name.json
To load data:
python manage.py loaddata fixtures/model_name.json --app scanface.tblfacescan
--indent X is optional.



python manage.py loaddata fixtures/resultados.json --app app.model_name

FUNCIONOU

python .\manage.py dumpdata scanface --indent 4 > .\resultados.json

python .\manage.py dumpdata scanface --indent 4 > .\resultados.json


UPDATE MODELS

python manage.py makemigrations --dry-run