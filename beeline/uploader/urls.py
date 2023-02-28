from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DatasetViewSet, RefNetworkViewSet

router = DefaultRouter()
router.register(r'datasets', DatasetViewSet)
router.register(r'ref-networks', RefNetworkViewSet)


urlpatterns = [
        path('', include(router.urls))
        ]
