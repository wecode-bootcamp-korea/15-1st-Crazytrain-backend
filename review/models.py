from django.db import models
from product.models import Product

class ReviewScore(models.Model):
    star = models.DecimalField(max_digits=1, decimal_places=None)

    class Meta:
        db_table = 'review_scores'

    def __str__(self):
        return self.star

class Review(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url   = models.URLField(max_length=500)
    content     = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, null=False)
    reviewscore = models.ForeignKey(ReviewScore, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'
