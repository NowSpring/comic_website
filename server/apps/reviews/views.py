from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# from .models import Comic, Review
from django.contrib.auth.models import User

from rest_framework import viewsets
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from django.db.models import Avg


class ReviewViewSet(viewsets.ModelViewSet):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        
        queryset = Review.objects.all()
        user_id = self.request.query_params.get('user', None)
        
        # ユーザーIDが指定されている場合は、そのユーザーに紐づくReviewを取得
        if user_id is not None:
            
            queryset = queryset.filter(user_id=user_id)
                
        return queryset

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def toggle_favorite(request, pk):
#     user = request.user
#     try:
#         comic = Comic.objects.get(pk=pk)
#         review, created = Review.objects.get_or_create(user=user, comic=comic)
#         review.isfavorite = request.data.get('isfavorite', False)
#         review.save()
#         return Response({'status': 'favorite updated'})
#     except Comic.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)