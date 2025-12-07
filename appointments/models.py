from django.db import models

# appointments/models.py
from django.db import models
from accounts.models import User, DoctorProfile, LaboratoryProfile

class Appointment(models.Model):
    """
    Renamed from Appointment to match OpenAPI spec naming (Reservation)
    """
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'     
        CONFIRMED = 'confirmed', 'Confirmed'   
        CANCELED = 'canceled', 'Canceled'   
        COMPLETED = 'completed', 'Completed' 

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_reservations')

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_reservations', null=True, blank=True)
    # laboratory = models.ForeignKey(LaboratoryProfile, on_delete=models.CASCADE, related_name='lab_reservations', null=True, blank=True)

    date = models.DateField()  # Separate date field
    time = models.TimeField()  # Separate time field
    
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.PENDING 
    )
    
    notes_from_patient = models.TextField(blank=True, null=True)
    notes_from_provider = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        target_name = ""
        if self.doctor:
            target_name = str(self.doctor)
            
        return f"Reservation for {self.patient.username} with {target_name} on {self.date} at {self.time}"
    
    class Meta:
        ordering = ['-created_at']
