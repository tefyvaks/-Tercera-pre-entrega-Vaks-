from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo= models.CharField(max_length=40)
    autor= models.CharField(max_length=40)
    genero= models.CharField(max_length=40)

class Socio(models.Model):
    nombreSocio= models.CharField(max_length=40)
    dni= models.IntegerField()

class Editorial(models.Model):
    nombreEditorial= models.CharField(max_length=40)
    
