from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='homepage'), 
    path('signup/', views.signup,name='signuppage'), 
    path('login/', views.userLogin,name='loginpage'), 
    path('passChange/', views.passChange,name='passchangepage'), 
    path('passChange2/', views.passChange2,name='passchange2page'), 
    path('logout/', views.userLogout,name='logoutpage'), 
    path('profile/', views.profile,name='profilepage'), 
     
]
 