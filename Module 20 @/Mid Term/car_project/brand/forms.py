from django.forms import forms
from brand.models import CarBrand

class Brand(forms.ModelForm):
    
    class Meta:
        model = CarBrand
        fields = '__all__'
