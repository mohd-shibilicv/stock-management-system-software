from rest_framework import serializers
from .models import Branch, ProductRequest


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'location', 'branch_code', 'contact_details', 'manager']
        read_only_fields = ['id']


class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRequest
        fields = ['id', 'branch', 'product', 'quantity', 'date_requested', 'fulfilled']
        read_only_fields = ['id', 'date_requested']
