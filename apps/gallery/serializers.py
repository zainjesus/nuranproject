from rest_framework import serializers
from .models import Gallery, Stages


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        exclude = ('description', )


class StagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stages
        fields = '__all__'