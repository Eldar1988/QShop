from django.db import models
from shop.models import Product
from seller.models import SellerShop


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviews')
    name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
