import email
from msilib.schema import Class
from pyexpat import model
from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveBigIntegerField()


#CREATE empleados
class EmpleadoClases(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email = models.EmailField()
    FechaNaciemiento = models.DateField()
    
