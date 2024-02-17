from rest_framework import viewsets
from reviews.models import Review
from reviews.api.serializers import ReviewSerializer
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