from django.urls import path,include
# from first_app.views import home
# from first_app import views
from . import views
urlpatterns = [
    path('', views.home),
]
