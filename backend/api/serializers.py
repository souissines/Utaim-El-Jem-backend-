from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Box

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('id', 'name', 'email', 'phone','message')

class BoxMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('id', 'name')
