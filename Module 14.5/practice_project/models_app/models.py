from django.db import models

# Create your models here.
class TestModelForm(models.Model):
    phone = models.BigIntegerField() 
    agree = models.BooleanField()
    name = models.CharField(max_length=255)
    date = models.DateField()
    dateTime = models.DateTimeField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField() 
    file = models.FileField(upload_to='files/')
    float = models.FloatField()
    # foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    # many_to_many_field = models.ManyToManyField(OtherModel)
    # one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    roll = models.IntegerField()
    # null_boolean_field = models.NullBooleanField() || not working
    null = models.BooleanField(null=True,blank=True) 
    student_id = models.SmallIntegerField() 
    massage = models.TextField()
    time = models.TimeField()
    url = models.URLField()
    uuid = models.UUIDField()