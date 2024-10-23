from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="nombre")
    description = models.TextField(max_length=300, verbose_name="descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="disponible")
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name="foto")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
