# Generated by Django 5.0.6 on 2024-08-08 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctor_available_time_doctor_available_time'),
        ('patient', '0002_alter_patient_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.TimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('✮', '✮'), ('✮✮', '✮✮'), ('✮✮✮', '✮✮✮'), ('✮✮✮✮', '✮✮✮✮'), ('✮✮✮✮✮', '✮✮✮✮✮')], max_length=5)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
