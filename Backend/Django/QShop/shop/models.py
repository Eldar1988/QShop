from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from seller.models import SellerShop
from QShop.settings import SHOP_UTILS as utils


class Category(models.Model):
    uid = models.CharField(max_length=255)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='categories')
    main_category = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child')
    title = models.CharField(max_length=255, db_index=True)
    label = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    image = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/categories/', 'image'),
                                  resize_source={'size': (200, 200), 'crop': 'scale'}, null=True, blank=True)
    miniature = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/categories/', 'image'),
                                      resize_source={'size': (200, 200), 'crop': 'scale'}, null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Brand(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='brands')
    title = models.CharField(max_length=255, db_index=True)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='brands')
    description = models.TextField(null=True, blank=True)
    logo = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/brands/', 'logo'),
                                 resize_source={'size': (200, 200), 'crop': 'scale'}, null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class CharacteristicType(models.Model):
    uid = models.CharField(max_length=255)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='characteristic_types')
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, blank=True, related_name='characteristic_types')
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Characteristic(models.Model):
    uid = models.CharField(max_length=255)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='characteristics')
    type = models.ForeignKey(CharacteristicType, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='characteristics')
    value = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.value


class Product(models.Model):
    uid = models.CharField(max_length=255)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    characteristics = models.ManyToManyField(Characteristic, blank=True, related_name='products')
    title = models.CharField(max_length=255, db_index=True)
    article = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    characteristic = models.TextField(null=True, blank=True)
    videos = models.TextField(max_length=255, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=16, decimal_places=0)
    old_price = models.DecimalField(null=True, blank=True, max_digits=16, decimal_places=0)
    purchase_price = models.IntegerField(null=True, blank=True)
    price_comment = models.CharField(null=True, blank=True, max_length=255)
    unit = models.CharField(max_length=20, null=True, blank=True)
    miniature = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/products/miniatures/', 'miniature'),
                                      null=True, blank=True, resize_source={'size': (300, 300), 'crop': 'scale'})
    miniature_url = models.URLField(null=True, blank=True)
    image_contain = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(default=5, null=True, blank=True)
    future = models.BooleanField(default=False)
    latest = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    in_stock_quantity = models.IntegerField(null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    shipping_detail = models.TextField(max_length=255, null=True, blank=True)
    views = models.IntegerField(default=0)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)


class VariationType(models.Model):
    uid = models.CharField(max_length=255)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='variation_types')
    title = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)


class Variation(models.Model):
    uid = models.CharField(max_length=255)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='variations')
    type = models.ForeignKey(VariationType, on_delete=models.SET_NULL, related_name='variations', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='variations')
    value = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        ordering = ('order',)


class ProductImage(models.Model):
    uid = models.CharField(max_length=255)
    shop = models.ForeignKey(SellerShop, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    image = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/products/images/', 'image'),
                                  null=True, blank=True, resize_source={'size': (1000, 1000), 'crop': 'scale'})
    image_url = models.URLField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='images')
    contain = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ('order',)
