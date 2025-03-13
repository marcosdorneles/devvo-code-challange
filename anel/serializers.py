from rest_framework import serializers
from .models import Anel


class AnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anel
        fields = '__all__'
