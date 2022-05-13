from django.db import models
from product.models import Product, Color, Variation
from django.core.validators import BaseValidator, MinValueValidator, MaxValueValidator

# Create your models here.
class Item(models.Model):
    name = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product_of_item", null=True, unique=True)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True, blank=True, related_name="variation_of_item")
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    size = models.CharField(max_length=1000, blank=True)
    price = models.FloatField(default=0, null=True, blank=True)
    color = models.OneToOneField(Color, on_delete=models.CASCADE, related_name='color_of_item', null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.name
