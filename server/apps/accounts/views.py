from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings


# Create your views here.
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def custom_obtain_jwt_token(request):
    # ここにカスタムJWTトークン生成コードを記述
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'password': user.password,
                'email': user.email,
                # その他必要なユーザー情報
            }
        })
    else:
        return Response({'error': 'Invalid Credentials'}, status=400)