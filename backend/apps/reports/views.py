from rest_framework import viewsets, permissions
from .serializers import ProductInflowSerializer, ProductOutflowSerializer
from .models import ProductInflow, ProductOutflow


class ProductInflowViewSet(viewsets.ModelViewSet):
    queryset = ProductInflow.objects.all()
    serializer_class = ProductInflowSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductOutflowViewSet(viewsets.ModelViewSet):
    queryset = ProductOutflow.objects.all()
    serializer_class = ProductOutflowSerializer
    permission_classes = [permissions.IsAuthenticated]
