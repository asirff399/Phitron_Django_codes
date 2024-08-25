from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewset,ReviewViewset,UserRegistrationApiView,UserLoginApiView,UserLogoutApiView,activate,PasswordChangeView


router = DefaultRouter()
router.register('list',CustomerViewset)
router.register('review',ReviewViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(),name='register'),
    path('login/', UserLoginApiView.as_view(),name='login'),
    path('logout/', UserLogoutApiView.as_view(),name='logout'),
    path('pass_change/', PasswordChangeView.as_view(),name='pass_change'),
    path('active/<uid64>/<token>/', activate, name = 'activate'),
]