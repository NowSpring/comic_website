from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comics.api import views

router = DefaultRouter()
router.register(r'comics', views.ComicViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path("comics/", views.ComicListView.as_view(), name = "comic_list"),
    path("comics/<int:pk>/", views.ComicDetailView.as_view(), name = "comic_detail"),    
]