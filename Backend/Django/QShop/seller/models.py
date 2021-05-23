from django.db import models


class Tariff(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=350)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    register_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('amount',)


class Seller(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True, blank=True, related_name='sellers')
    active = models.BooleanField(default=True)
    uid = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=2000)
    mailing = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to='seller/avatars/')
    register_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name:
            return self.name
        return self.uid

    class Meta:
        ordering = ('-register_date',)


class SellerShop(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='shops')
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


# class SellerShopSettings(models.Model):
#     seller_shop = models.ForeignKey(SellerShop, on_delete=models.CASCADE, related_name='settings')
#     currency_code = models.CharField(max_length=5)
