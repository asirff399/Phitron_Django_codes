from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.AddCar.as_view(), name='add_car'),
    path('delete/<int:id>', views.DeleteCar.as_view(), name='delete'),
    path('edit/<int:id>', views.UpdateCar.as_view(), name='edit'),
    path('details/<int:id>', views.CarDetailsView.as_view(), name='details'),
    path('details/buy/<int:id>', views.CarOrder, name='car_buy'),
]     