from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.users.views import UserRegisterViewSet, LogoutView, LoginViewSet, RefreshViewSet
from apps.products.views import ProductViewSet, DamagedProductViewSet
from apps.branches.views import BranchViewSet, ProductRequestViewSet, BranchProductViewSet
from apps.suppliers.views import SupplierViewSet
from apps.reports.views import ProductInflowViewSet, ProductOutflowViewSet


router = DefaultRouter()

# Auth
router.register(r'register', UserRegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'refresh', RefreshViewSet, basename='refresh')

# Store
router.register(r'products', ProductViewSet, basename='products')
router.register(r'damaged-products', DamagedProductViewSet, basename='damaged_products')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'product-inflow', ProductInflowViewSet, basename='product_inflow')
router.register(r'product-outflow', ProductOutflowViewSet, basename='product_outflow')

# Branch
router.register(r'branches', BranchViewSet, basename='branches')
router.register(r'branch-products', BranchProductViewSet, basename='branch_products')
router.register(r'product-requests', ProductRequestViewSet, basename='product_requests')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/logout/', LogoutView.as_view({'post': 'logout'}), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
