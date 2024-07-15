from django.db import models
import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=100, verbose_name="Servicio")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    categoria = models.CharField(max_length=255,null=False, blank=False,verbose_name="Categoría")
    precio = models.IntegerField(blank=True, null=True, verbose_name="Precio")
    
    def __str__(self):
        return self.servicio
from django.db import models
from django.contrib.auth.models import User

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='elementos', on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    @property
    def total_precio(self):
        return self.cantidad * self.servicio.precio

    def __str__(self):
        return f'{self.cantidad} x {self.servicio.servicio}'
