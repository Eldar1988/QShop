from django.contrib import admin
from .models import Seller, SellerShop, SellerNotification


@admin.register(SellerNotification)
class SellerNotificationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'date', 'personal')
    list_filter = ('personal', 'date', 'update')
    search_fields = ('title', 'seller__name', 'seller__uid')
    save_as = True


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'active', 'tariff', 'balance', 'register_date')
    search_fields = ('uid', 'name', 'phone', 'tariff')
    list_filter = ('active', 'register_date', 'update')
    save_as = True


@admin.register(SellerShop)
class SellerShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'active', 'register_date')
    search_fields = ('uid', 'seller__name', 'title', 'url')
    list_filter = ('active', 'register_date', 'update')
    save_as = True
