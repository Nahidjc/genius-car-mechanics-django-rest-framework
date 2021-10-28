from django.shortcuts import render
from rest_framework import viewsets
from .models import Services
from .serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions, serializers, status
# Create your views here.


class ServiceViewSet(ListAPIView):
    serializer_class = ServiceSerializer
    # def get_queryset(self):
    #     return Services.objects.all()
    permission_classes = (permissions.AllowAny,)
    queryset = Services.objects.all()

    # def list(self, request):
    #     queryset = Services.objects.all()
    #     serializer = ServiceSerializer(queryset, many=True)
    #     return Response(serializer.data)
