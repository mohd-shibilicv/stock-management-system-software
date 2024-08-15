from rest_framework import viewsets, permissions
from .serializers import BranchSerializer, ProductRequestSerializer
from .models import Branch, ProductRequest


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductRequestViewSet(viewsets.ModelViewSet):
    queryset = ProductRequest.objects.all()
    serializer_class = ProductRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
