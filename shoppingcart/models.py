from django.db import models
from user.models import User
from prodect.models import Product, OptionSize, OptionColor, Option

class Cart(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=256, default=1)
    size     = models.ForeignKey(OptionSize, on_delete=models.CASCADE)
    color    = models.ForeignKey(OptionColor, on_delete=models.CASCADE)
    price    = models.ForeignKey(Option, on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'

