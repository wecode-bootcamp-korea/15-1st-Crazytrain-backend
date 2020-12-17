from django.db import models
from product.models import Product


class User(models.Model):
    email         = models.EmailField(max_length=100, unique=True)
    password      = models.CharField(max_length=100)
    nickname      = models.CharField(max_length=15, unique=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    gender        = models.BooleanField(null=True)
    birth_date    = models.DateField(auto_now=False, null=True)
    profile_image = models.URLField(max_length=256,null=True)
    note          = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email


class History(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    product    = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'histories'
