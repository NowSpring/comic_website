from rest_framework import viewsets
from comics.models import Comic
from .serializers import ComicSerializer



class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer


    