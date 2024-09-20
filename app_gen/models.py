from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Customer(models.Model):
    names         = models.CharField(max_length=150, verbose_name='Nombres')
    dni           = models.CharField(max_length=150, unique=True, verbose_name='Dni')
    date_creation = models.DateTimeField(auto_now=True)
    date_update   = models.DateTimeField(auto_now_add=True)
    address       = models.CharField(max_length=100, verbose_name='Direccion')    
    city          = models.CharField(max_length=100, verbose_name='Ciudad')    
    commune       = models.CharField(max_length=100, verbose_name='Comuna')    
    email         = models.CharField(max_length=100, verbose_name='Email')    
    phone         = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], verbose_name= 'Telefono')    

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name        = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table            = 'empresa'
        ordering            = ['dni']


class Categoria(models.Model):
    pass

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name        = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table            = 'categoria'
        ordering            = ['dni']

class Producto(models.Model):
    code          = models.CharField(max_length=150, unique=True, verbose_name='Codigo')
    description   = models.CharField(max_length=150, verbose_name='Descripcion')
    names         = models.CharField(max_length=150, verbose_name='Nombres')
    amount        = models.IntegerField(max_length=20 , verbose_name='Cantidad')
    price         = models.IntegerField(max_length=15 , verbose_name='Precio')