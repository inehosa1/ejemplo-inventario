# Create your views here.
from rest_framework import viewsets
from .models import Product, Alert
from .serializers import ProductSerializer, AlertSerializer
from .paginate import CustomPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo products.
    """
    queryset = Product.objects.prefetch_related(
        "alerts"
    ).all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination


class AlertViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el modelo Alert.
    """
    queryset = Alert.objects.select_related(
        "product"
    ).all()
    serializer_class = AlertSerializer
