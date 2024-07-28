from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Transaction
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .forms import DepositeForm,WithdrawForm
from .constants import DEPOSIT,WITHDRAWAL
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from datetime import datetime
from django.db.models import Sum
# Create your views here.

def send_email(user,amount,subject,template):
    message = render_to_string(template,{
        'user':user,
        'amount':amount,
    })
    send_email = EmailMultiAlternatives(subject,'',to=[user.email])
    send_email.attach_alternative(message,'text/html')
    send_email.send()

class TransactionCreatMixin(LoginRequiredMixin,CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                'account': self.request.user.account
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'title':self.title
        })
        return context
    
class DepositMoneyView(TransactionCreatMixin):
    form_class = DepositeForm
    title = 'Deposite Money'

    def get_initial(self):
        initial = {'transaction_type':DEPOSIT}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save( update_fields =['balance'] )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_email(self.request.user,amount,'Deposite Message','deposite_email.html')
        return super().form_valid(form)
    
class WithdrawMoneyView(TransactionCreatMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type':WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance -= amount
        account.save( update_fields =['balance'] )

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )
        send_email(self.request.user,amount,'Withdrawal Message','withdrawal_email.html')
        return super().form_valid(form)

class TransactionReportView(LoginRequiredMixin,ListView):
    template_name = 'transaction_report.html'
    model = Transaction
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account = self.request.user.account
        )

        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str,'%y-%m-%d').date()
            end_date = datetime.strptime(end_date_str,'%y-%m-%d').date()

            queryset = queryset.filter(timestamp__date__gte=start_date,timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date,timestamp__date__lte=end_date
            ).aaggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {'account':self.request.user.account}
        )
        return context