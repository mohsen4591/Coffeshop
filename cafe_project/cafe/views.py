from rest_framework import viewsets
from .models import User, Admin, Storage, Vertical, Product, Order, OrderProduct
from .serializers import UserSerializer, AdminSerializer, StorageSerializer, VerticalSerializer, ProductSerializer, OrderSerializer, OrderProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class VerticalViewSet(viewsets.ModelViewSet):
    queryset = Vertical.objects.all()
    serializer_class = VerticalSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
