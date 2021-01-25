from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.name


# class User(models.Model):
#     class Meta:
#        username = models.CharField(max_length=100)
#        first 
#         fields = (
#             'id', 'username', 'first_name', 'last_name', 'email',
#             'last_login', 'date_joined'
#         )
