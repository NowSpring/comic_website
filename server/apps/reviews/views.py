from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comic, Review
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request, pk):
    user = request.user
    try:
        comic = Comic.objects.get(pk=pk)
        review, created = Review.objects.get_or_create(user=user, comic=comic)
        review.isfavorite = request.data.get('isfavorite', False)
        review.save()
        return Response({'status': 'favorite updated'})
    except Comic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)