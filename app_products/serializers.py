from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id']

class ProductCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
