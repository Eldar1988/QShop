from rest_framework import generics
from .models import Seller, SellerShop
from .serializers import SellerSerializer, SellerShopSerializer


class SellerDetailView(generics.RetrieveAPIView):
    """Get seller detail by user_id"""
    queryset = Seller.objects.all()
    lookup_field = 'uid'
    serializer_class = SellerSerializer


class SellerCreateView(generics.CreateAPIView):
    """Create seller"""
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
