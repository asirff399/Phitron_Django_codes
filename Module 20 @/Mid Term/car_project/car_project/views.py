from django.shortcuts import render
from brand.models import CarBrand
from car.models import Cars
def main(request):
    return render(request,'base.html')

def home(request,brand_slug=None):
    data = Cars.objects.all()
    if brand_slug is not None:
        brand = CarBrand.objects.get(slug = brand_slug)
        data = Cars.objects.filter(brand=brand)
    brand = CarBrand.objects.all()
    return render(request,'home.html',{'data':data,'brand':brand})
