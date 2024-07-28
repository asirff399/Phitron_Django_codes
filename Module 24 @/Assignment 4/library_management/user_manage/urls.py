from django.urls import path,include
from .views import DepositMoneyView,WithdrawMoneyView,TransactionReportView
urlpatterns = [
    path('deposit/', DepositMoneyView.as_view(), name='deposit'),
    path('withdraw/', WithdrawMoneyView.as_view(), name='withdraw'),
    path('report/', TransactionReportView.as_view(), name='transaction_report'),
    
]   