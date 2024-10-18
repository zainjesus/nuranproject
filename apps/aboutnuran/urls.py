from django.urls import path
from .views import AboutRetrieveAPIView


urlpatterns = [
    path('about/', AboutRetrieveAPIView.as_view(), name='about-retrieve')
]