from django.urls import path
from .views import custom_obtain_jwt_token

urlpatterns = [
    # 既存のURLパターン...
    path('', custom_obtain_jwt_token, name='custom_signin'),
]