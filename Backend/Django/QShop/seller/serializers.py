from rest_framework import serializers
from .models import Seller, SellerShop, SellerNotification


class SellerShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerShop
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    shops = SellerShopSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = '__all__'


class SellerShopListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerShop
        fields = ('id', 'title', 'logo', 'url')


class SellerNotificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerNotification
        fields = ('id', 'title', 'text', 'date')
