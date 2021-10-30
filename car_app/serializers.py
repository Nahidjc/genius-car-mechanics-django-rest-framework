from django.db.models import fields
from rest_framework import serializers
from .models import Services


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name', 'description',
                  'price', 'imgUrl', 'created', 'updated']


class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services


class ServiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        lookup_field = 'id'
