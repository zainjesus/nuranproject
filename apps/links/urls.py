from django.urls import path
from .views import LinksRetrieveAPIView


urlpatterns = [
    path('links/', LinksRetrieveAPIView.as_view(), name='links-retrieve')
]
