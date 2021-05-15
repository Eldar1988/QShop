from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from seller.models import SellerShop
from QShop.settings import SHOP_UTILS as utils


class Category(models.Model):
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories')
    main_category = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child')
    title = models.CharField(max_length=255, db_index=True)
    label = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    image = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/categories/', 'image'),
                                  resize_source={'size': (200, 200), 'crop': 'scale'})
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Brand(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='brands')
    description = models.TextField(null=True, blank=True)
    logo = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/categories/', 'image'),
                                 resize_source={'size': (200, 200), 'crop': 'scale'})
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
