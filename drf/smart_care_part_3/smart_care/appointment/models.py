from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.

APPOINTMENT_STATUS=[
    ('Pending','Pending'),
    ('Running','Running'),
    ('Compleated','Compleated'),
]
APPOINTMENT_TYPE=[
    ('Offline','Offline'),
    ('Online','Online'),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=10,choices=APPOINTMENT_TYPE)
    appointment_status = models.CharField(max_length=10,choices=APPOINTMENT_STATUS,default="Pending")
    symptom = models.TextField(default=None)
    time = models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Doctor: {self.doctor.user.first_name}; Patient: {self.patient.user.first_name}"