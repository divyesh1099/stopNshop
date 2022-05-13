from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to = 'shop/%Y/%m/%d/', blank=True, unique = True, default = 'shop/default.png')

    def __str__(self):
        return self.name