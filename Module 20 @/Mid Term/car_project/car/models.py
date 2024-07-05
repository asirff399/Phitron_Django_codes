from django.db import models
from django.contrib.auth.models import User
from brand.models import CarBrand
# Create your models here.
class Cars(models.Model):
    image = models.ImageField(upload_to='car/media/uploads/',blank=True,null=True)
    name = models.CharField(max_length=100)
    body = models.TextField()
    price = models.IntegerField()
    model = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=10)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    brand = models.ForeignKey(CarBrand,on_delete=models.CASCADE)
  
    def __str__(self): 
        return self.name
    
class Comment(models.Model):
    car=models.ForeignKey(Cars,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name 
    
  
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
    car=models.ForeignKey(Cars,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
    quantity = models.PositiveIntegerField(default=1,blank=True,null=True)
    order_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f'{{self.car.name}} by {{self.user.name}}' 
    
   
        

