from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewset,UserRagistration,Activate,UserLoginApiView,UserLogoutApiView

router = DefaultRouter()
router.register('list', PatientViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',UserRagistration.as_view(),name='register'),
    path('login/',UserLoginApiView.as_view(),name='login'),
    path('logout/',UserLogoutApiView.as_view(),name='logout'),
    path('active/<uid64>/<token>/',Activate,name='activate'), 
] 