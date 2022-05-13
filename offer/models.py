from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length=500)
    details = models.TextField(blank=True)
    discount = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.name
    