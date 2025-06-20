from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CreateCheckoutSessionView

routers = DefaultRouter()
routers.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(routers.urls)),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]