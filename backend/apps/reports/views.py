from datetime import datetime
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, F
from .serializers import (
    ProductInflowSerializer,
    ProductOutflowSerializer,
    InwardQtyReportSerializer,
    OutwardQtyReportSerializer,
    BranchWiseQtyReportSerializer,
    ExpiredProductReportSerializer,
    OpenedProductReportSerializer,
    ClosedProductReportSerializer,
    DailyReportSerializer,
    ProductDetailsReportSerializer,
    SupplierWiseProductReportSerializer,
)
from apps.products.models import Product, DamagedProduct
from apps.branches.models import BranchProduct
from .models import ProductInflow, ProductOutflow


class ProductInflowViewSet(viewsets.ModelViewSet):
    queryset = ProductInflow.objects.all()
    serializer_class = ProductInflowSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductOutflowViewSet(viewsets.ModelViewSet):
    queryset = ProductOutflow.objects.all()
    serializer_class = ProductOutflowSerializer
    permission_classes = [permissions.IsAuthenticated]


class InwardQtyReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        inflows = (
            ProductInflow.objects.values("product__name", "supplier__name", "expiry_date")
            .annotate(total_quantity=Sum("quantity_received"))
            .order_by("-total_quantity")
        )
        serializer = InwardQtyReportSerializer(inflows, many=True)
        return Response(serializer.data)


class OutwardQtyReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        outflows = (
            ProductOutflow.objects.values("product__name", "branch__name", "expiry_date")
            .annotate(total_quantity=Sum("quantity_sent"))
            .order_by("-total_quantity")
        )
        serializer = OutwardQtyReportSerializer(outflows, many=True)
        return Response(serializer.data)


class BranchWiseQtyReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        branch_products = (
            BranchProduct.objects.values("branch__name", "product__name")
            .annotate(total_quantity=Sum("quantity"))
            .order_by("branch__name", "-total_quantity")
        )
        serializer = BranchWiseQtyReportSerializer(branch_products, many=True)
        return Response(serializer.data)


class ExpiredProductReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        today = datetime.now().date()
        expired_products = (
            ProductInflow.objects.filter(expiry_date__lte=today)
            .values("product__name", "expiry_date")
            .annotate(quantity=Sum("quantity_received"))
            .order_by("expiry_date")
        )
        serializer = ExpiredProductReportSerializer(expired_products, many=True)
        return Response(serializer.data)


class SupplierWiseProductReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        supplier_products = (
            ProductInflow.objects.values("supplier__name", "product__name")
            .annotate(total_quantity=Sum("quantity_received"))
            .order_by("supplier__name", "-total_quantity")
        )
        serializer = SupplierWiseProductReportSerializer(supplier_products, many=True)
        return Response(serializer.data)


class OpenedProductReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        opened_products = (
            BranchProduct.objects.filter(status="active")
            .values("product__name", "branch__name")
            .annotate(quantity=Sum("quantity"))
            .order_by("-quantity")
        )
        serializer = OpenedProductReportSerializer(opened_products, many=True)
        return Response(serializer.data)


class ClosedProductReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        closed_products = (
            BranchProduct.objects.filter(status="inactive")
            .values("product__name", "branch__name")
            .annotate(quantity=Sum("quantity"))
            .order_by("-quantity")
        )
        serializer = ClosedProductReportSerializer(closed_products, many=True)
        return Response(serializer.data)


class DailyReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        today = datetime.now().date()
        inflows = ProductInflow.objects.filter(date_received=today)
        outflows = ProductOutflow.objects.filter(date_sent=today)
        data = {
            "inflows": inflows,
            "outflows": outflows,
        }
        serializer = DailyReportSerializer(data)
        return Response(serializer.data)


class ProductDetailsReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.annotate(
            total_inflow=Sum("productinflow__quantity_received"),
            total_outflow=Sum("productoutflow__quantity_sent"),
            closing_stock=F("quantity"),
        ).values("name", "sku", "total_inflow", "total_outflow", "closing_stock")
        serializer = ProductDetailsReportSerializer(products, many=True)
        return Response(serializer.data)
