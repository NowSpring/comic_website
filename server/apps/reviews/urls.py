from django.urls import path
from .views import toggle_favorite

urlpatterns = [
    # 既存のURLパターン...
    path('', toggle_favorite, name='toggle-favorite'),
]