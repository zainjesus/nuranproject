from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryViewSet, StagesViewSet

router = DefaultRouter()
router.register(r'gallery', GalleryViewSet)
router.register(r'stages', StagesViewSet)

urlpatterns = [
    path('', include(router.urls))
]