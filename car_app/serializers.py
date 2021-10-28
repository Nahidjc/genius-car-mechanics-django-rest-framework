from django.db.models import fields
from rest_framework import serializers
from .models import Services

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Services
        fields=['id','name','description','price','imgUrl','created', 'updated']