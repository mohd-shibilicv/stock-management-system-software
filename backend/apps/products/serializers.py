from rest_framework import serializers
from .models import Product, DamagedProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "sku",
            "description",
            "price",
            "quantity",
            "category",
            "brand",
            "opening_stock",
        ]
        read_only_fields = ["id"]


class DamagedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamagedProduct
        fields = ['id', 'product', 'quantity', 'reason', 'date_reported']
        read_only_fields = ['id', 'date_reported']
