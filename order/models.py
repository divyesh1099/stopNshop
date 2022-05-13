from django.db import models
import uuid
from product.models import Product
from django.contrib.auth.models import User

# Create your models here.



class Order(models.Model):
    generated_order_id = models.CharField(max_length=100,  default=uuid.uuid4, unique=True)
    products = models.ManyToManyField(Product, related_name='product_of_order')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    address = models.TextField()
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    zip = models.PositiveBigIntegerField()
    phonenumber = models.PositiveBigIntegerField()
    amount = models.PositiveIntegerField()
    dispatched = models.BooleanField()
    dispatched_timestamp = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField()
    delivered_timestamp = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField()
    cancelled = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.id)

