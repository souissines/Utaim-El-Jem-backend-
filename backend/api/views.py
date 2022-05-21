from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import Box
from rest_framework.response import Response

from .serializers import BoxMiniSerializer, BoxSerializer


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

    def list(self, request, *args, **kwargs):
        boxes = Box.objects.all()
        serializer = BoxMiniSerializer(boxes, many=True)
        return Response(serializer.data)
