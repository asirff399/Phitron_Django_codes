from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.taskModel,name='taskmodelpage'),
    path('edit/<int:id>', views.Edit,name='editpage'),
    path('delete/<int:id>', views.delete,name='deletepage'),
]