from rest_framework import serializers
from .models import AboutCompany


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        exclude = ('id', 'aboutCompany', 'aboutProject')