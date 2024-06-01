from django import forms
from django.core import validators

class contactForm(forms.Form):
    # name = forms.CharField(label = 'Full Name :' , initial= 'Your Name', help_text='Total length must be within 70 characters' , required=False , disabled=True )
    name = forms.CharField(label = 'Full Name :', help_text='Total length must be within 70 characters' , required=False , widget= forms.Textarea(attrs={'id':'textarea','class':'class class-2','placeholder':'Enter Your Name'}) )
    # file = forms.FileField(label='Upload File')
    email = forms.EmailField(label = 'User Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget= forms.NumberInput)
    birthday = forms.CharField(widget= forms.DateInput(attrs={'type':'date'})) 
    appointment = forms.CharField(widget= forms.DateInput(attrs={'type':'datetime-local'})) 
    check = forms.BooleanField()
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect) 
    EXTRA = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=EXTRA ,widget=forms.CheckboxSelectMultiple) 


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valuName = self.cleaned_data['name']
#     #     if len(valuName) < 10:
#     #         raise forms.ValidationError('Enter a name with at least 10 characters')
#     #     return valuName
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError('Your email must contain .com')      
#     #     return valemail
    
#     def clean(self):
#         clean_data = super().clean()
#         valuName = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valuName) < 10:
#             raise forms.ValidationError('Enter a name with at least 10 characters')
#         elif '.com' not in valemail:
#             raise forms.ValidationError('Your email must contain .com')  

def len_check(valu):
    if len(valu) < 10:
        raise forms.ValidationError("Enter text at least 10 chars")
class StudentData(forms.Form):
    # name = forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(30,message='Enter a name with max 10 characters')])
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Enter a name with at least 10 characters')])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check]) 
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='Enter a valid email')]) 
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35,message="Maximum requared age is 35"),validators.MinValueValidator(20,message="Minimum requared age is 20")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpeg','png'],message="File extension must be ended with .pdf | .jpeg | .png")])
      

class passwordValidationproject(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)
    confirm_password = forms.CharField(widget= forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        
        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        
        if len(val_name) < 15:
            raise forms.ValidationError("Name must at least 15 characters")
        if val_conpass != val_pass:
            raise forms.ValidationError("Possword doesn't match") 