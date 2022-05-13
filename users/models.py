from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'user/profile/default.jpg', upload_to = 'user/profile/%Y/%m/%d/')
    phonenumber = models.PositiveBigIntegerField(blank = True, default=0000000000)
    state = models.CharField(max_length = 100, blank = True, default="Maharashtra")
    city = models.CharField(max_length = 100, blank = True)
    zip_code = models.PositiveIntegerField(blank=True, default=400709)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username