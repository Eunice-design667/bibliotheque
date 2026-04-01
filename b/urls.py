from django.urls import path, include
from rest_framework.routers import DefaultRouter
from serializers import livreSerializer, empruntSerializer, userSerializer

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='livre')

urlpatterns = [
    path('', include(router.urls))
]
