from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.name

    # blog model


class Blog(models.Model):
    email = models.EmailField()
    image = models.CharField(max_length=250, default="")
    description = models.TextField(max_length=450, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
