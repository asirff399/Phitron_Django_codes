from django.urls import path,include
from . import views
urlpatterns = [  
    path('', views.album,name='albumpage'), 
    path('edit/<int:id>', views.edit_data,name='editpage'), 
    path('delete/<int:id>', views.delete_data,name='deletepage'), 
]