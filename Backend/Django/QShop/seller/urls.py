from django.urls import path
from . import views


urlpatterns = [
    path('get_seller/<uid>/', views.SellerDetailView.as_view()),
    path('create_seller/', views.SellerCreateView.as_view()),
    path('update_seller/<uid>/', views.UpdateSellerView.as_view()),
    path('notifications/', views.NotificationsView.as_view()),
    path('shops/', views.SellerShopListView.as_view())
]
