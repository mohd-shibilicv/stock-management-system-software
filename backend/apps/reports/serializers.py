from rest_framework import serializers
from .models import ProductInflow, ProductOutflow


class ProductInflowSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    supplier_name = serializers.CharField(source="supplier.name", read_only=True)

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
    product_name = serializers.CharField(source="product.name", read_only=True)
    branch_name = serializers.CharField(source="branch.name", read_only=True)

    class Meta:
        model = ProductOutflow
        fields = [
            "id",
            "product",
            "product_name",
            "branch",
            "branch_name",
            "quantity_sent",
            "expiry_date",
            "date_sent",
        ]
        read_only_fields = ["id", "date_sent"]


class InwardQtyReportSerializer(serializers.Serializer):
    product__name = serializers.CharField()
    supplier__name = serializers.CharField()
    expiry_date = serializers.DateField()
    total_quantity = serializers.IntegerField()


class OutwardQtyReportSerializer(serializers.Serializer):
    product__name = serializers.CharField()
    branch__name = serializers.CharField()
    expiry_date = serializers.DateField()
    total_quantity = serializers.IntegerField()


class BranchWiseQtyReportSerializer(serializers.Serializer):
    branch__name = serializers.CharField()
    product__name = serializers.CharField()
    total_quantity = serializers.IntegerField()


class ExpiredProductReportSerializer(serializers.Serializer):
    product__name = serializers.CharField()
    expiry_date = serializers.DateField()
    quantity = serializers.IntegerField()


class SupplierWiseProductReportSerializer(serializers.Serializer):
    supplier__name = serializers.CharField()
    product__name = serializers.CharField()
    total_quantity = serializers.IntegerField()


class OpenedProductReportSerializer(serializers.Serializer):
    product__name = serializers.CharField()
    branch__name = serializers.CharField()
    quantity = serializers.IntegerField()


class ClosedProductReportSerializer(serializers.Serializer):
    product__name = serializers.CharField()
    branch__name = serializers.CharField()
    quantity = serializers.IntegerField()


class DailyReportSerializer(serializers.Serializer):
    inflows = ProductInflowSerializer(many=True)
    outflows = ProductOutflowSerializer(many=True)


class ProductDetailsReportSerializer(serializers.Serializer):
    name = serializers.CharField()
    sku = serializers.CharField()
    total_inflow = serializers.IntegerField()
    total_outflow = serializers.IntegerField()
    closing_stock = serializers.IntegerField()
