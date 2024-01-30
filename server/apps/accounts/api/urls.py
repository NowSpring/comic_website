from django.urls import path
from .views import CreateUserView
from accounts.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'signup', views.CreateUserView)

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
]
