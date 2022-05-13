from django.db import models
# from django.contrib.auth.models import AbstractUser
from product.models import Product
# Create your models here.
# class User(AbstractUser):
#     pass

class CarouselImage(models.Model):
    i1 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True, default = 'carousel_default/1.jpg')
    i2 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True, default = 'carousel_default/2.jpg')
    i3 = models.ImageField(upload_to='carousel/%Y/%m/%d/', blank=True, unique = True, default = 'carousel_default/3.jpg')

class Gallery(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_of_gallery', blank=True, unique=True)
    
    def __str__(self):
        return self.product.name