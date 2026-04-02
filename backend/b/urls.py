from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, LivreViewSet, EmpruntViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'livres', LivreViewSet, basename='livre')
router.register(r'emprunts', EmpruntViewSet, basename='emprunt')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
