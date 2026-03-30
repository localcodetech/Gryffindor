from django.db import models

# Create your models here.

class Product(models.Model):
    name =  models.CharField(max_length=100)
    image = models.ImageField(upload_to="/images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=200)
