from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Client(models.Model):
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
        verbose_name        = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table            = 'cliente'
        ordering            = ['dni']
class Category(models.Model):
    name         = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name        = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table            = 'categoria'
        # ordering            = ['dni']
class Product(models.Model):
    code          = models.CharField(max_length=150, unique=True, verbose_name='Codigo')
    description   = models.CharField(max_length=150, verbose_name='Descripcion')
    name         = models.CharField(max_length=150, verbose_name='Nombres')
    amount        = models.IntegerField(verbose_name='Cantidad')
    price         = models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return self.name 
    class Meta:
        verbose_name        = 'Producto'
        verbose_name_plural = 'Productos'
        db_table            = 'producto'
class Sale(models.Model):
    cli         = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal    = models.DecimalField(default=0.00, max_digits=9 , decimal_places=2)
    iva         = models.DecimalField(default=0.00, max_digits=9 , decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=9 , decimal_places=2)

    def __str__(self):
        return self.cli.names 
    class Meta:
        verbose_name        = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table            = 'venta'
class DetSale(models.Model):
    sale           = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod           = models.ForeignKey(Product, on_delete=models.CASCADE)
    price          = models.DecimalField(default=0.00, max_digits=9 , decimal_places=2)
    cant           = models.IntegerField(default=0)
    subtotal       = models.DecimalField(default=0.00, max_digits=9 , decimal_places=2)

    def __str__(self):
        return self.prod.name
    class Meta:
        verbose_name        = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        db_table            = 'detventa'