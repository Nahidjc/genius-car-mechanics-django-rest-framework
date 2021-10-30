from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from .models import Services
from .serializers import ServiceSerializer, DeleteSerializer, ServiceDetailsSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, serializers, status
from rest_framework.decorators import api_view
from rest_framework import generics

# Create your views here.


class ServiceViewSet(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (permissions.AllowAny,)

    # def get_queryset(self):
    #     return Services.objects.all()
    # permission_classes = (permissions.AllowAny,)
    # queryset = Services.objects.all()

    # def list(self, request):
    #     queryset = Services.objects.all()
    #     serializer = ServiceSerializer(queryset, many=True)
    #     return Response(serializer.data)


class ServiceDelete(DestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = DeleteSerializer
    lookup_field = 'id'


class ServiceDetailsView(RetrieveUpdateAPIView):
    serializer_class = ServiceDetailsSerializer
    queryset = Services.objects.all()
    lookup_field = 'id'
