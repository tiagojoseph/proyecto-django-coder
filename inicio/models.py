from django.db import models

class Auto (models.Model):
    marca = models.CharField (max_length= 20)
    modelo = models.CharField (max_length= 20)
    año = models.IntegerField ()
