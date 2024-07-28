from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.AddBookView.as_view(), name='add_book'),
    path('details/<int:id>', views.BookDetailsView.as_view(), name='details'),
    path('details/edit/<int:id>', views.UpdateBookView.as_view(), name='edit'),
    path('details/delete/<int:id>', views.DeleteBookView.as_view(), name='delete'),
    path('details/borrow/<int:id>', views.BorrowBook, name='borrow'),
    path('details/return/<int:id>', views.ReturnBook, name='return'),
    path('order_report/', views.OrderReportView.as_view(), name='order_report'), 
]   