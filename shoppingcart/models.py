from django.db import models
from user.models import User
from product.models import Product, OptionSize, OptionColor, Option

class Cart(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    color    = models.ForeignKey(OptionColor, on_delete=models.CASCADE, null=True)
    option    = models.ForeignKey(Option, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'

