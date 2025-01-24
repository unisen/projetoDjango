# your_custom_migration.py
import json
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command

def load_file(apps, schema_editor):

    YourModel = apps.get_model('your_app', 'YourModel')

    with open('resultados.json') as json_file:
        data = json.load(json_file)
        for p in data:
            # create YourModel object and save it to database
            your_model = YourModel.objects.create(key=p['key'], name=p['name'], tier=['tier']) 


class Migration(migrations.Migration):

    dependencies = [
        ('manager', 'your_previous_migration_that_you_depend'),
    ]

    operations = [
        migrations.RunPython(load_file, None)
    ]