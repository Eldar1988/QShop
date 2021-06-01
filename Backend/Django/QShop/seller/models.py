from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from QShop.settings import SHOP_UTILS as utils


class Seller(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    tariff = models.DecimalField(max_digits=12, decimal_places=2, default=130)
    active = models.BooleanField(default=True)
    uid = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=2000)
    mailing = models.BooleanField(default=False)
    avatar = ThumbnailerImageField(upload_to=utils.path_and_rename('shop/products/miniatures/', 'miniature'),
                                      null=True, blank=True, resize_source={'size': (300, 300), 'crop': 'scale'})
    register_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name:
            return self.name
        return self.uid

    class Meta:
        ordering = ('-register_date',)


class SellerShop(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='shops')
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='seller/logos/', null=True, blank=True)
    favicon = models.ImageField(upload_to='seller/favicons/', null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-register_date',)


class SellerNotification(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')
    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    personal = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date',)



# class SellerShopSettings(models.Model):
#     seller_shop = models.ForeignKey(SellerShop, on_delete=models.CASCADE, related_name='settings')
#     currency_code = models.CharField(max_length=5)
