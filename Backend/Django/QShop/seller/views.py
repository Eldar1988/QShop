from rest_framework import generics
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

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


class UpdateSellerAvatarView(generics.UpdateAPIView):
    """Update seller avatar"""
    parser_classes = [MultiPartParser, FormParser]
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = 'uid'


class UpdateSellerView(generics.UpdateAPIView):
    """Update seller"""
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = 'uid'
