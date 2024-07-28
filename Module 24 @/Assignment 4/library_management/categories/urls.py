from django.urls import path,include
from .views import CategoryView
# from .views import category

urlpatterns = [
    # path('', category,name='category'),
    path('', CategoryView.as_view(),name='category'),
]
 