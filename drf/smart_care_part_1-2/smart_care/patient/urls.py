from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewset

router = DefaultRouter()
router.register('list', PatientViewset)

urlpatterns = [
    path('', include(router.urls)),
]