from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134043ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134043", Testconnectors134043ViewSet, basename="testconnectors134043"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
