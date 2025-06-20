from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

routers = DefaultRouter()
routers.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(routers.urls)),
]