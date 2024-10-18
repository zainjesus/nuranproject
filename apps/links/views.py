from rest_framework.generics import RetrieveAPIView
from .models import Links
from .serializers import LinksSerializer


class LinksRetrieveAPIView(RetrieveAPIView):
    serializer_class = LinksSerializer

    def get_object(self):
        return Links.objects.first()
