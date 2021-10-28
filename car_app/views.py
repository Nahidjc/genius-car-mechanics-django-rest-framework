from django.shortcuts import render
from rest_framework import viewsets
from .models import Services
from .serializers import ServiceSerializer
# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    def get_queryset(self):
        return Services.objects.all()