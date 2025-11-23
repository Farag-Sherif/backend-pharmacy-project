from django.db import models

# appointments/models.py
from django.db import models
from accounts.models import User, DoctorProfile, LaboratoryProfile

class Appointment(models.Model):
    
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'     
        APPROVED = 'APPROVED', 'Approved'   
        REJECTED = 'REJECTED', 'Rejected'   
        COMPLETED = 'COMPLETED', 'Completed' 
        CANCELLED = 'CANCELLED', 'Cancelled' 

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_appointments', null=True, blank=True)
    laboratory = models.ForeignKey(LaboratoryProfile, on_delete=models.CASCADE, related_name='lab_appointments', null=True, blank=True)

    appointment_time = models.DateTimeField() 
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.PENDING 
    )
    
    notes_from_patient = models.TextField(blank=True, null=True)
    
    notes_from_provider = models.TextField(blank=True, null=True)

    def __str__(self):
        target_name = ""
        if self.doctor:
            target_name = str(self.doctor)
        elif self.laboratory:
            target_name = str(self.laboratory)
            
        return f"موعد لـ {self.patient.username} مع {target_name} في {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"
