from django.db import models
from menu.models import SubCategory


class Package(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'packages'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'brands'

    def __str__(self):
        return self.name

class Sale(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'sales'

    def __str__(self):
        return self.name

class Product(models.Model):
    name              = models.CharField(max_length=30)
    information       = models.CharField(max_length=200)
    sub_category      = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    information_image = models.URLField(max_length=256, null=True)
    package           = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    brand             = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    sale              = models.ForeignKey(Sale, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class OptionSize(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'option_sizes'

    def __str__(self):
        return self.name

class OptionColor(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'option_colors'

    def __str__(self):
        return self.name

class Option(models.Model):
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_size  = models.ForeignKey(OptionSize, on_delete=models.CASCADE)
    option_color = models.ForeignKey(OptionColor, on_delete=models.CASCADE)
    price        = models.FloatField()

    class Meta:
        db_table = 'options'

    def __str__(self):
        return self.price

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url     = models.URLField(max_length=256)
    

    class Meta:
        db_table = 'product_images'
