from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.conf import settings
from shop.models import *
import uuid
from colorfield.fields import ColorField
from offer.models import Offer
import math
# Create Your Models Here

class Shipping(models.Model):
    shipping = models.FloatField(default=100)

class Size(models.Model):
    size = models.CharField(max_length=1000, blank=True, unique=True)

    class Meta:
        ordering = ['size']
    
    def __str__(self):
        return self.size

class Material(models.Model):
    material = models.CharField(max_length=1000, blank=True, unique=True)

    class Meta:
        ordering = ['material']
    
    def __str__(self):
        return self.material

class Color(models.Model):
    color = ColorField(default = '#FF0000')
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length = 100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to = 'types/')
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="type_of_product")
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="offer_of_product", blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    stock = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)], help_text="Will Be Automatically Calculated")
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, related_name = "shop_of_product", blank=True)
    class Meta:
        ordering = ['edited']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Price Calculation
        # temporary_price = float(math.inf)
        try:
        #     for variation in self.variations.all():
        #         if temporary_price >= variation.price:
        #             temporary_price = variation.price
        #     self.price = temporary_price
            # Stock Calculation
            self.stock = 0
            for variation in self.variations.all():
                self.stock += variation.stock
        except Exception as e:
            print("Product Model Exception is: ", e)

        # Mandatory
        super(Product, self).save(*args, **kwargs)

class Variation(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    product = models.ForeignKey(Product, related_name="variations", on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to ='variations/%Y/%m/%d/', blank = True, null = True)
    size = models.ForeignKey(Size, related_name="size_of_variation", on_delete=models.CASCADE, blank=True, null=True)
    color = models.ForeignKey(Color, related_name="color_of_variation", on_delete=models.CASCADE, blank=True, null=True)
    material = models.ForeignKey(Material, related_name="material_of_variation", on_delete=models.CASCADE, blank=True, null=True)
    dimension_LxWxH = models.CharField(max_length = 200, blank=True, null=True, help_text="(in centimeters (cms))")
    date_first_available = models.DateField(auto_now_add=True, blank=True, null=True)
    manufacturer_name = models.CharField(max_length=200, blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True, default='Mens')
    manufacturer_address = models.CharField(max_length=500, blank=True, null=True)
    packer_address = models.CharField(max_length=500, blank=True, null=True)
    item_weight = models.FloatField(blank=True, null=True, help_text="(in grams (gms))")
    net_quantity = models.IntegerField(blank=True, null=True)
    included_components = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)
    edited = models.DateTimeField(auto_now = True)
    generated_variation_id = models.CharField(max_length=100,  default=uuid.uuid4, unique=True)

    class Meta:
        ordering = ['edited']

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name if self.name else "Variation: Stock" + str(self.stock) + ", Price: " + str(self.price)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', default='products/default.jpg')