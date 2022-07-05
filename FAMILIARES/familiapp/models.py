from django.db import models

class Padre(models.Model):
    nombre = models.CharField(max_length=50)
    
    fecha_nacimiento = models.DateField()

    años = models.IntegerField()

class Madre(models.Model):
    nombre = models.CharField(max_length=50)
    
    fecha_nacimiento = models.DateField()

    años = models.IntegerField()

class Hermano (models.Model):
    nombre = models.CharField(max_length=50)
    
    fecha_nacimiento = models.DateField()
