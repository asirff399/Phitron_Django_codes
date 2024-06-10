# Generated by Django 5.0.6 on 2024-06-05 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_alter_album_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 5, 9, 8, 34, 870830)),
        ),
    ]