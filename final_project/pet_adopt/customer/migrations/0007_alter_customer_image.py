# Generated by Django 5.1 on 2024-08-23 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.FileField(upload_to='customer-images'),
        ),
    ]