from rest_framework import viewsets
from .models import Gallery, Stages
from .serializers import GallerySerializer, StagesSerializer

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class StagesViewSet(viewsets.ModelViewSet):
    queryset = Stages.objects.all()
    serializer_class = StagesSerializer