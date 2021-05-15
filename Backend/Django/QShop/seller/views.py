from rest_framework import generics
from .models import Seller, SellerShop
from .serializers import SellerSerializer, SellerShopSerializer


class SellerDetailView(generics.RetrieveAPIView):
    """Get seller detail by user_id"""
    queryset = Seller.objects.all()
    lookup_field = 'user_id'
    serializer_class = SellerSerializer

