# Generated by Django 5.0.6 on 2024-07-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('Borrow', 'Borrow'), ('Return', 'Return')], max_length=20, null=True),
        ),
    ]