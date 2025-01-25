from django.db import models

# Create your models here.


class Recipes(models.Model):
    name = models.CharField(max_length=120, default='')
    pub_date = models.DateTimeField('date published')
    style = models.CharField(max_length=200, default='')
    brewer = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=20, default='All Grain')
    version = models.CharField(max_length=20, default='1')
    batch_size = models.DecimalField(decimal_places=2, max_digits=8, default=0.0)
    boil_size = models.DecimalField(decimal_places=2, max_digits=8, default=0.0)
    boil_time = models.DecimalField(decimal_places=1, max_digits=4, default=0.0)
    efficiency = models.DecimalField(decimal_places=1, max_digits=4, default=75.0)
    ibu = models.DecimalField(decimal_places=1, max_digits=4, default=0.0)
    abv = models.DecimalField(decimal_places=2, max_digits=4, default=0.0)
    notes = models.TextField(default='')
    carbonation = models.DecimalField(decimal_places=2, max_digits=4, default=0.0)
    primary_age = models.DecimalField(decimal_places=1, max_digits=4, default = 0)
    secondary_age = models.DecimalField(decimal_places=1, max_digits=4, default = 0)
    age = models.DecimalField(decimal_places=1, max_digits=4, default = 0)
    __fermentables = []
  
    @classmethod
    def create(cls,attr):
        recipe = cls()
        # do something with the book
        for k in Recipes._meta.fields:
            if  k.name in attr:
                setattr(recipe,k.name,attr[k.name])
        return recipe
    
    
class FaceLogin(models.Model):
    verified = models.CharField(max_length=60)
    distance = models.CharField(max_length=60)
    threshold = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    detector_backend = models.CharField(max_length=60)
    similarity_metric = models.CharField(max_length=60)
    facial_areas = models.CharField(max_length=400)
    time = models.CharField(max_length=60)
     

class Scanface(models.Model):
    
    # `verified`, `distance`, `threshold`, `model`, `detector_backend`, `similarity_metric`, `facial_areas`, `time`
    # {'verified': True, 'distance': 0.5461194975162682, 'threshold': 0.68, 'model': 'VGG-Face', 'detector_backend': 'opencv', 'similarity_metric': 'cosine', 'facial_areas': '', 'time': 3.8}
    
    #files = models.CharField(max_length=200, default='')
    verified = models.CharField(max_length=200, default='')
    distance = models.CharField(max_length=100, default='')
    threshold = models.DecimalField(max_digits=3, decimal_places=2)
    model = models.CharField(max_length=200, default='')
    detector_backend = models.CharField(max_length=100, default='')
    similarity_metric = models.CharField(max_length=100, default='')
    facial_areas = models.CharField(max_length=500, default='')
    time = models.CharField(max_length=100, default='')
    """ date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now=True) """
    
    @classmethod
    def create(cls,attr):
        recipe = cls()
        # do something with the book
        for k in Scanface._meta.fields:
            if  k.name in attr:
                setattr(recipe,k.name,attr[k.name])
        return recipe
    