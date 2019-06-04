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


class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scheme
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Studio
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = '__all__'
