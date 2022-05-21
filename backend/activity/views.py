from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from activity.models import Activity
from activity.serializers import ActivitySerializer
# Create your views here.




class ActivityViewSet (viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def post(self, request, *args, **kwargs):
        activity_photo = request.data['activity_photo']
        title = request.data['title']
        Activity.objects.create(title=title, activity_photo=activity_photo)
        return HttpResponse({'message': 'Activity created'}, status=200)
    def __delete__(self, instance):

        activity = Activity.objects.get(id)
        activity.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)