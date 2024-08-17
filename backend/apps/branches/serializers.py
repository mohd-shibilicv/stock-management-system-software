from rest_framework import serializers
from .models import Branch, ProductRequest, BranchProduct


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'location', 'branch_code', 'contact_details', 'manager']
        read_only_fields = ['id']


class BranchProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchProduct
        fields = ['id', 'product_name', 'product_sku', 'product_category', 'product_brand', 'quantity', 'last_updated']


class UpdateBranchProductQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchProduct
        fields = ['quantity']


class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRequest
        fields = ['id', 'branch', 'product', 'quantity', 'date_requested', 'fulfilled']
        read_only_fields = ['id', 'date_requested']
