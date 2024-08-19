from rest_framework import serializers
from .models import ProductInflow, ProductOutflow


class ProductInflowSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = ProductInflow
        fields = [
            "id",
            "product",
            "product_name",
            "supplier",
            "supplier_name",
            "quantity_received",
            "manufacturing_date",
            "expiry_date",
            "date_received",
        ]
        read_only_fields = ["id", "date_received"]


class ProductOutflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOutflow
        fields = [
            "id",
            "product",
            "branch",
            "quantity_sent",
            "expiry_date",
            "date_sent",
        ]
        read_only_fields = ["id"]
