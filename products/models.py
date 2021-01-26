from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    image = models.FilePathField(path="/Users/zoe/portfolio/django_ecommerce/products/static/img")