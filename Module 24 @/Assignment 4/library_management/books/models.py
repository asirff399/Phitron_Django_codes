from django.db import models
from accounts.models import User,UserAccount
from categories.models import CategoryModel
from .constants import ORDER_TYPE
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='books/images',blank=True,null=True)
    borrowing_price = models.IntegerField()
    quantity = models.PositiveIntegerField(default=10)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    book=models.ForeignKey(Books,on_delete=models.CASCADE,related_name='reviews',blank=True,null=True)
    name = models.CharField(max_length=30)
    rating = models.CharField(max_length=10,choices=(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'), 
    ),null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name   

class Order(models.Model):
    account = models.ForeignKey(UserAccount,related_name='order',on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
    balance_after_order = models.DecimalField(decimal_places=2,max_digits=12)
    order_type = models.CharField(max_length=20,choices=ORDER_TYPE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
     
    
    @staticmethod
    def user_has_borrowed_book(user, book):
        if isinstance(user, User):
            user = user.account
        return Order.objects.filter(account=user, book=book, order_type='Borrow').exists()
    
    @staticmethod
    def user_has_return_book(user, book):
        if isinstance(user, User):
            user = user.account
        return Order.objects.filter(account=user, book=book, order_type='Return').exists()
     
    def __str__(self):   
        return f'{self.book.title} by {self.account.user}' 