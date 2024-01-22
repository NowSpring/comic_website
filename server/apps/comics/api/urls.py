from django.urls import path
from comics.api import views

urlpatterns = [
    path("comics/", views.ComicListView.as_view(), name = "comic_list"),
    path("comics/<int:pk>/", views.ComicDetailView.as_view(), name = "comic_detail"),    
]