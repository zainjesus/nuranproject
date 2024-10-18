from rest_framework.generics import RetrieveAPIView
from .models import AboutCompany
from .serializers import AboutCompanySerializer


class AboutRetrieveAPIView(RetrieveAPIView):
    serializer_class = AboutCompanySerializer

    def get_object(self):
        return AboutCompany.objects.first()
