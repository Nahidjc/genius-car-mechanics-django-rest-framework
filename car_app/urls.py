
from django.urls import path
from car_app import views
urlpatterns = [
     path('services/',views.ServiceViewSet.as_view({'get': 'list'}),name='services' ),
]
