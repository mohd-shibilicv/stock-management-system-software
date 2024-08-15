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
            "barcode_image"
        ]
        read_only_fields = ["id", "barcode_image"]
    
    def create(self, validated_data):
        # Create the product instance
        product = Product.objects.create(**validated_data)
        
        # Generate the barcode after the initial save
        product.generate_barcode()
        
        # Save the product again with the generated barcode image
        product.save()

        return product


class DamagedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamagedProduct
        fields = ['id', 'product', 'quantity', 'reason', 'date_reported']
        read_only_fields = ['id', 'date_reported']
