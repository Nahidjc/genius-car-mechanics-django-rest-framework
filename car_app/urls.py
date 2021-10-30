
from django.urls import path
from car_app import views
urlpatterns = [
    path('services/',
         views.ServiceViewSet.as_view(), name='services'),
    path('delete-service/<id>/',
         views.ServiceDelete.as_view(), name='delete-service'),
    path('service/<id>/', views.ServiceDetailsView.as_view(), name='details')
]
