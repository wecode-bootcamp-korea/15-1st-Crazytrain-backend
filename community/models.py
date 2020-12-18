from django.db import models

from product.models import Product
from user.models import User


class HouseSize(models.Model):
    size = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'house_sizes'

    def __str__(self):
        return self.size

class HouseStyle(models.Model):
    style = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'house_styles'

    def __str__(self):
        return self.style

class HousingType(models.Model):
    type = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'housing_types'

    def __str__(self):
        return self.type

class Space(models.Model):
    space = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'spaces'

    def __str__(self):
        return self.space

class Post(models.Model):
    content      = models.CharField(max_length=200)
    product      = models.ForeignKey(Product, on_delete=models.CASCADE)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    house_size   = models.ForeignKey(HouseSize, on_delete=models.CASCADE)
    house_style  = models.ForeignKey(HouseStyle, on_delete=models.CASCADE)
    housing_type = models.ForeignKey(HousingType, on_delete=models.CASCADE)
    space        = models.ForeignKey(Space, on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'posts'

class PostImage(models.Model):
    url  = models.URLField(max_length=256)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_images'

class Hashtag(models.Model):
    name = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'hashtags'

    def __str__(self):
        return self.name

class PostHashtag(models.Model):
    post    = models.ForeignKey('Post', on_delete=models.CASCADE)
    hashtag = models.ForeignKey('Hashtag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_hashtags'
