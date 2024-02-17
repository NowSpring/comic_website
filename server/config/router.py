from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.comics.views import ComicViewSet
from apps.reviews.views import ReviewViewSet

router = DefaultRouter()
router.register(r'comics', ComicViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'accounts', A)


