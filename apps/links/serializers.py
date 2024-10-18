from rest_framework import serializers
from .models import Links


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        exclude = ('id', )