from rest_framework import generics
from django.contrib.auth.models import User
from accounts.api.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer