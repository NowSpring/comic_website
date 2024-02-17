from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comics.api import views

router = DefaultRouter()
router.register(r'comics', views.ComicViewSet)

urlpatterns = [
    path("", include(router.urls)), 
]