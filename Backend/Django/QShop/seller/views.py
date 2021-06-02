from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from .models import Seller, SellerShop, SellerNotification
from .serializers import SellerSerializer, SellerShopSerializer, SellerNotificationsSerializer


class SellerDetailView(generics.RetrieveAPIView):
    """Get seller detail by user_id"""
    queryset = Seller.objects.all()
    lookup_field = 'uid'
    serializer_class = SellerSerializer


class SellerCreateView(generics.CreateAPIView):
    """Create seller"""
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class UpdateSellerView(generics.UpdateAPIView):
    """Update seller"""
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    lookup_field = 'uid'


class NotificationsView(generics.ListAPIView):
    """Seller notifications"""
    queryset = SellerNotification.objects.all()[:20]
    serializer_class = SellerNotificationsSerializer
