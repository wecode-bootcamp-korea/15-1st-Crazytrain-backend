from django.db import models

from product.models import Product
from user.models import User

class Post(models.Model):
    content = models.CharField(max_length=200),
    product = models.ForeignKey(Product, on_delete=models.CASCADE),
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    posted_image = models.ForeignKey(PostImage, on_delete=models.CASCADE),
    created_at = models.DateTimeField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.created_at

class PostImage(models.Model):
    url = models.URLField(max_length=256)

    class Meta:
        db_table = 'post_images'

class Hashtag(models.Model):
    name = models.CharField(max_length=45,null=True)

    class Meta:
        db_table = 'hashtags'

    def __str__(self):
        return self.name

class PostHashtag(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE),
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posthashtags'

