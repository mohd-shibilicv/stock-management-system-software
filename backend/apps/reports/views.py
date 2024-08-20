from datetime import datetime
from dateutil.relativedelta import relativedelta
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
    BranchDailyReportSerializer,
    BranchExpiredProductReportSerializer,
    BranchProductDetailsReportSerializer,
)
from apps.products.models import Product
from apps.branches.models import Branch, BranchProduct, ProductRequest
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
            ProductInflow.objects.values(
                "product__name", "supplier__name", "expiry_date"
            )
            .annotate(total_quantity=Sum("quantity_received"))
            .order_by("-total_quantity")
        )
        serializer = InwardQtyReportSerializer(inflows, many=True)
        return Response(serializer.data)


class OutwardQtyReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        outflows = (
            ProductOutflow.objects.values(
                "product__name", "branch__name", "expiry_date"
            )
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


class BranchDailyReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        branch = request.user.managed_branch
        today = datetime.now().date()

        inflows = ProductRequest.objects.filter(
            branch=branch, status="fulfilled", date_requested__date=today
        )

        data = {
            "inflows": inflows,
        }

        serializer = BranchDailyReportSerializer(data)
        return Response(serializer.data)


class BranchProductDetailsReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        branch = request.user.managed_branch
        branch_products = BranchProduct.objects.filter(branch=branch).select_related(
            "product"
        )

        products = [
            {
                "name": bp.product.name,
                "sku": bp.product.sku,
                "quantity": bp.quantity,
                "status": bp.status,
            }
            for bp in branch_products
        ]

        serializer = BranchProductDetailsReportSerializer(products, many=True)
        return Response(serializer.data)


class BranchExpiredProductReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        branch = request.user.managed_branch
        today = datetime.now().date()

        expired_products = (
            BranchProduct.objects.filter(
                branch=branch, product__productinflow__expiry_date__lte=today
            )
            .annotate(
                product_name=F("product__name"),
                expiry_date=F("product__productinflow__expiry_date"),
            )
            .values("product_name", "expiry_date", "quantity")
        )

        serializer = BranchExpiredProductReportSerializer(expired_products, many=True)
        return Response(serializer.data)


class DashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Get query parameters for time period filtering
        period = request.query_params.get("period", "daily")

        # Calculate date range based on the period
        end_date = datetime.now().date()
        if period == "daily":
            start_date = end_date
        elif period == "monthly":
            start_date = end_date - relativedelta(months=1)
        elif period == "yearly":
            start_date = end_date - relativedelta(years=1)
        else:
            return Response({"error": "Invalid period specified"}, status=400)

        # Fetch data for different sections of the dashboard
        total_products = Product.objects.count()
        total_branches = Branch.objects.count()

        inflow_data = ProductInflow.objects.filter(
            date_received__range=[start_date, end_date]
        ).aggregate(
            total_inflow=Sum("quantity_received"),
            total_inflow_value=Sum("quantity_received" * "product__price"),
        )

        outflow_data = ProductOutflow.objects.filter(
            date_sent__range=[start_date, end_date]
        ).aggregate(
            total_outflow=Sum("quantity_sent"),
            total_outflow_value=Sum("quantity_sent" * "product__price"),
        )

        top_products = Product.objects.annotate(
            total_outflow=Sum("productoutflow__quantity_sent")
        ).order_by("-total_outflow")[:5]

        low_stock_products = Product.objects.filter(quantity__lt=10).count()

        branch_stock = (
            BranchProduct.objects.values("branch__name")
            .annotate(total_stock=Sum("quantity"))
            .order_by("-total_stock")[:5]
        )

        expired_products = (
            ProductInflow.objects.filter(expiry_date__lte=end_date)
            .values("product__name")
            .annotate(total_expired=Sum("quantity_received"))
            .order_by("-total_expired")[:5]
        )

        # Prepare the response data
        response_data = {
            "total_products": total_products,
            "total_branches": total_branches,
            "total_inflow": inflow_data["total_inflow"] or 0,
            "total_inflow_value": inflow_data["total_inflow_value"] or 0,
            "total_outflow": outflow_data["total_outflow"] or 0,
            "total_outflow_value": outflow_data["total_outflow_value"] or 0,
            "top_products": [
                {"name": product.name, "total_outflow": product.total_outflow or 0}
                for product in top_products
            ],
            "low_stock_products": low_stock_products,
            "branch_stock": list(branch_stock),
            "expired_products": list(expired_products),
        }

        return Response(response_data)
