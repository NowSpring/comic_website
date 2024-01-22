from rest_framework import generics
from comics.models import Comic
from comics.api.serializers import ComicSerializer


class ComicListView(generics.ListCreateAPIView):
    
    queryset = Comic.objects.all().order_by("title")
    serializer_class = ComicSerializer
    
    
class ComicDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer