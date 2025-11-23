from django.db import models

# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    class Role(models.TextChoices):
        PATIENT = 'PATIENT', 'Patient'
        DOCTOR = 'DOCTOR', 'Doctor'
        PHARMACY = 'PHARMACY', 'Pharmacy'
        LAB = 'LAB', 'Laboratory'
        ADMIN = 'ADMIN', 'Admin'

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.PATIENT)
    
    is_approved = models.BooleanField(default=False)
    
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.username
    
class Specialization(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PatientProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient_profile')
    medical_history = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class DoctorProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor_profile')
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True, null=True) # نبذة عن الطبيب
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # سعر الكشف
    license_number = models.CharField(max_length=100, unique=True, null=True, blank=True) # رقم رخصة مزاولة المهنة

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

class PharmacyProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='pharmacy_profile')
    address = models.CharField(max_length=255)
    license_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username 

class LaboratoryProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='lab_profile')
    address = models.CharField(max_length=255)
    license_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
