
from django.urls import path
from car_app import views
urlpatterns = [
    path('services/',
         views.ServiceViewSet.as_view(), name='services'),
    path('add-service/', views.create_service, name='create-service'),
]
