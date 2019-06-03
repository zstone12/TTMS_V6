from rest_framework import serializers
from app01 import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Play
        fields = '__all__'
