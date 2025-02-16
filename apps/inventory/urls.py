from rest_framework.routers import DefaultRouter
from apps.inventory.views import ProductViewSet, AlertViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]