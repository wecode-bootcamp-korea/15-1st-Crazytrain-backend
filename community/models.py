from django.db import models

from product.models import Product
from user.models import User


class HouseSize(models.Model):
    size = models.CharField(max_length=45)

    class Meta:
        db_table = 'house_sizes'

    def __str__(self):
        return self.size

class HouseStyle(models.Model):
    style = models.CharField(max_length=45)

    class Meta:
        db_table = 'house_styles'

    def __str__(self):
        return self.style

class HousingType(models.Model):
    type = models.CharField(max_length=45)

    class Meta:
        db_table = 'housing_types'

    def __str__(self):
        return self.type

class Space(models.Model):
    space = models.CharField(max_length=45)

    class Meta:
        db_table = 'spaces'

    def __str__(self):
        return self.space

class Post(models.Model):
    product      = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    house_size   = models.ForeignKey(HouseSize, on_delete=models.CASCADE,null=True)
    house_style  = models.ForeignKey(HouseStyle, on_delete=models.CASCADE,null=True)
    housing_type = models.ForeignKey(HousingType, on_delete=models.CASCADE,null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'posts'

class PostBlock(models.Model):
    image   = models.URLField(max_length=256)
    content = models.CharField(max_length=200)
    space   = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_blocks'

#
# class Hashtag(models.Model):
#     hashtag   = models.CharField(max_length=45,null=True)
#     postblock = models.ForeignKey(PostBlock, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'hashtags'
#
#     def __str__(self):
#         return self.hashtag
#
# class PostHashtag(models.Model):
#     post    = models.ForeignKey(Post, on_delete=models.CASCADE)
#     hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'post_hashtags'

