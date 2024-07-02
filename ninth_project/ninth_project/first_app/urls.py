from django.urls import path,include
from . import views
urlpatterns = [
    # path('',views.home,name='homepage'),
    path('',views.set_session),
    # path('get_cookie/',views.get_cookie),
    path('get_session/',views.get_session),
    # path('del_cookie/',views.delete_cookie),
    path('del_session/',views.delete_session),
] 
