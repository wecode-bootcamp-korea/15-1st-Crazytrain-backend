from django.db import models
from user.models import User
from product.models import Product, OptionSize, OptionColor, Option

class Cart(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(max_length=256, default=1)
    size     = models.ForeignKey(OptionSize, on_delete=models.CASCADE, null=True)
    color    = models.ForeignKey(OptionColor, on_delete=models.CASCADE, null=True)
    price    = models.ForeignKey(Option, on_delete=models.CASCADE)
    checked  = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'carts'

