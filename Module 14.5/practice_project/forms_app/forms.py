from django import forms
import datetime
class testform(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3})) 
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_day = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))  
    birth_choice = [2004,2005,2006,2007,2008,2009,2010]
    birth_day = forms.DateField(widget=forms.SelectDateWidget(years=birth_choice))  
    valu = forms.DecimalField()
    email_address = forms.EmailField(required = False)
    message = forms.CharField(max_length = 10)
    email_address = forms.EmailField(label='Please enter your email address') 
    first_name = forms.CharField(initial='Your name')
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today) 
    choice = {
        'B':'Blue',
        'G':'Green',
        'R':'Red'
    } 
    color = forms.ChoiceField(choices=choice) 
    color = forms.ChoiceField(widget=forms.RadioSelect,choices=choice)  
    color = forms.MultipleChoiceField(choices=choice)   
    color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choice)   
    roll = forms.IntegerField(help_text = "Enter 6 digit roll number") 
    password = forms.CharField(widget = forms.PasswordInput()) 
