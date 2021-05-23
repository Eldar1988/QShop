from rest_framework import serializers
from .models import Seller, SellerShop


class SellerShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerShop
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    shops = SellerShopSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerShop
        fields = ('id', 'title', 'logo', 'url')
