from django.urls import path
from . import views


urlpatterns = [
    path('seller_detail/<user_id>/', views.SellerDetailView.as_view())
]
