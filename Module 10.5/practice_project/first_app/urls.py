from django.urls import path
from . import views
urlpatterns = [
    path('', views.first),
    path('home/', views.home),
    path('product/', views.product),
    path('about/', views.about),
    path('contact/', views.contact),
]