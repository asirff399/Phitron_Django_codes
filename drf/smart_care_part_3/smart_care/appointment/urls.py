from django.urls import include,path
from rest_framework import routers
from .views import AppointmentViewSet


router = routers.DefaultRouter()
router.register('', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 
