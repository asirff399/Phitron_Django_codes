from django import forms
from .models import Books,Review,Order

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ['author']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','rating','body']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['__all__']

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') 
        super().__init__(*args, **kwargs)
        self.fields['order_type'].disabled = True
        self.fields['order_type'].widget = forms.HiddenInput() 

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_order = self.account.balance
        return super().save() 