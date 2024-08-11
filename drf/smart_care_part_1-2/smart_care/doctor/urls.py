from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewset,SpecializationViewset,DesignationViewset,AvailableTimeViewset,ReviewViewset

router = DefaultRouter()
router.register('list', DoctorViewset)
router.register('specialization', SpecializationViewset)
router.register('designation', DesignationViewset)
router.register('available_time', AvailableTimeViewset)
router.register('review', ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]