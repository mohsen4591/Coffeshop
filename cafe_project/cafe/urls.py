from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AdminViewSet, StorageViewSet, VerticalViewSet, ProductViewSet, OrderViewSet, OrderProductViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'storage', StorageViewSet)
router.register(r'verticals', VerticalViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-products', OrderProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
