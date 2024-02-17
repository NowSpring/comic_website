from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reviews.api import views

router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]