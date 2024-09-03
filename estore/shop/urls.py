from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CategoryViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
# router.register(r'products', ProductViewSet)
router.register(r"orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
