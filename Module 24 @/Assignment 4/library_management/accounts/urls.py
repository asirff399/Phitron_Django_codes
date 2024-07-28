from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserLogoutView,UserProfileUpdateView,UserProfile

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(),name='signup'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogoutView.as_view(),name='logout'),
    path('update_profile/', UserProfileUpdateView.as_view(),name='update_profile'),
    path('profile/',UserProfile,name='profile'), 
]
 