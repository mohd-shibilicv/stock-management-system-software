from rest_framework import serializers
from .models import ProductInflow, ProductOutflow


class ProductInflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInflow
        fields = [
            "id",
            "product",
            "supplier",
            "quantity_received",
            "manufacturing_date",
            "expiry_date",
            "date_received",
        ]
        read_only_fields = ["id"]


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
