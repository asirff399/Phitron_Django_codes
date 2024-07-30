from django import forms
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from .forms import BooksForm,ReviewForm
from .models import Books,Review,Order
from accounts.models import UserAccount
from django.contrib import messages
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.mixins import LoginRequiredMixin
# from user_manage.forms import DepositeForm,WithdrawForm
from .constants import ORDER_TYPE
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponseForbidden
# Create your views here.
class AddBookView(CreateView):
    model = Books
    title = 'Add Book'
    template_name = 'add.html'
    form_class = BooksForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request,'Book added successfully.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Book add failed.')
        return super().form_invalid(form)
    
class UpdateBookView(UpdateView):
    title = 'Edit Book'
    model = Books
    form_class = BooksForm
    template_name = 'edit.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

class DeleteBookView(DeleteView):
    model = Books
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class BookDetailsView(DetailView):
    model = Books
    template_name = 'details.html'
    pk_url_kwarg = 'id'
    
    def post(self,request,*args, **kwargs):
        review_form = ReviewForm(data = self.request.POST)
        book = self.get_object()

        if not Order.user_has_borrowed_book(request.user, book):
            return HttpResponseForbidden("You can only review books that you have borrowed.")
        
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book
            new_review.user = request.user
            new_review.save()
            return self.get(request,*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object 
        reviews = book.reviews.all()
        review_form = ReviewForm()
        context["reviews"] = reviews 
        context["review_form"] = review_form 
        return context
    
def send_email(user,amount,subject,template):
    message = render_to_string(template,{
        'user':user,
        'amount':amount,
    })
    send_email = EmailMultiAlternatives(subject,'',to=[user.email])
    send_email.attach_alternative(message,'text/html')
    send_email.send()

@login_required
def BorrowBook(request,id):
    book = get_object_or_404(Books,id = id)
    user_ac = get_object_or_404(UserAccount,user = request.user)

    if book.quantity > 0 and user_ac.balance >= book.borrowing_price:
        book.quantity -= 1
        user_ac.balance -= book.borrowing_price
        book.save()
        user_ac.save()

        Order.objects.create(
            account = user_ac,
            book=book, 
            balance_after_order = user_ac.balance,
            order_type = ORDER_TYPE['Borrow']  
        )

        messages.success(request,
            f'{book.title} was borrowed successfully. '
            f' {book.borrowing_price}$ was deducted from your account.'
        )
    else:
        messages.error(request,
            'Unable to borrow book. Check availability or your balance.'
        )
    send_email(request.user,book.borrowing_price,'Borrowed Book Message','borrow_email.html')
    return redirect('order_report')

@login_required
def ReturnBook(request,id):
    book = get_object_or_404(Books,id = id)
    user_ac = get_object_or_404(UserAccount,user = request.user)

    book.quantity += 1
    user_ac.balance += book.borrowing_price
    book.save()
    user_ac.save()

    Order.objects.create(
        account = user_ac,
        book=book,
        balance_after_order = user_ac.balance,
        order_type = ORDER_TYPE['Return']  
    ) 

    messages.success(request,
        f'{book.title} was returned successfully.'
        f'  {book.borrowing_price}$ was return to your account.'
    )
    send_email(request.user,book.borrowing_price,'Return Book Message','return_email.html')
    return redirect('order_report')


class OrderReportView(LoginRequiredMixin,ListView):
    template_name = 'order_report.html'
    model = Order
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
            self.balance = Order.objects.filter(
                timestamp__date__gte=start_date,timestamp__date__lte=end_date
            ).aaggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'account':self.request.user.account,
                'balance': self.balance
            }
        )
        return context

