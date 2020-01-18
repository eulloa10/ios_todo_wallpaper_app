
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from wplapp.models import Fish
from wplapp.serializers import FishSerializer

# Create your views here.
class FishViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
