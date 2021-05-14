from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mailing = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to='seller/avatars/')
    register_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-register_date',)


class SellerShop(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='shops')
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='seller/logos/', null=True, blank=True)
    favicon = models.ImageField(upload_to='seller/favicons/', null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-register_date',)


