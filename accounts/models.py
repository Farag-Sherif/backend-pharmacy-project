from django.db import models

# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    class Role(models.TextChoices):
        PATIENT = 'patient', 'Patient'
        DOCTOR = 'doctor', 'Doctor'
        PHARMACY = 'pharmacy', 'Pharmacy'
        LAB = 'laboratory', 'Laboratory'
        RADIOLOGY = 'radiology', 'Radiology'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.PATIENT)
    
    is_approved = models.BooleanField(default=False)
    
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Specialization(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PatientProfile(models.Model):
    
    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='patient_profile')
    medical_history = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class DoctorProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='doctor_profile')
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)  # نبذة/description
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # fee
    license_number = models.CharField(max_length=100, unique=True, null=True, blank=True)
    experience = models.IntegerField(default=0, help_text="Years of experience")
    address = models.TextField(blank=True, null=True)

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

class RadiologyProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='radiology_profile')
    address = models.CharField(max_length=255)
    license_number = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

class WorkingHours(models.Model):
    """
    Working hours for pharmacies, laboratories, and radiology centers
    """
    class DayChoices(models.TextChoices):
        SATURDAY = 'Saturday', 'Saturday'
        SUNDAY = 'Sunday', 'Sunday'
        MONDAY = 'Monday', 'Monday'
        TUESDAY = 'Tuesday', 'Tuesday'
        WEDNESDAY = 'Wednesday', 'Wednesday'
        THURSDAY = 'Thursday', 'Thursday'
        FRIDAY = 'Friday', 'Friday'
    
    owner_id = models.IntegerField()  # ID of pharmacy/lab/radiology
    owner_type = models.CharField(max_length=20, choices=[
        ('pharmacy', 'Pharmacy'),
        ('laboratory', 'Laboratory'),
        ('radiology', 'Radiology')
    ])
    day = models.CharField(max_length=20, choices=DayChoices.choices)
    open_time = models.TimeField()
    close_time = models.TimeField()
    
    class Meta:
        unique_together = ['owner_id', 'owner_type', 'day']
        verbose_name_plural = 'Working Hours'
    
    def __str__(self):
        return f"{self.owner_type} {self.owner_id} - {self.day}: {self.open_time}-{self.close_time}"

class DoctorAvailability(models.Model):
    """
    Availability slots for doctors
    """
    class DayChoices(models.TextChoices):
        SATURDAY = 'Saturday', 'Saturday'
        SUNDAY = 'Sunday', 'Sunday'
        MONDAY = 'Monday', 'Monday'
        TUESDAY = 'Tuesday', 'Tuesday'
        WEDNESDAY = 'Wednesday', 'Wednesday'
        THURSDAY = 'Thursday', 'Thursday'
        FRIDAY = 'Friday', 'Friday'
    
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='availabilities')
    day = models.CharField(max_length=20, choices=DayChoices.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
        verbose_name_plural = 'Doctor Availabilities'
    
    def __str__(self):
        return f"{self.doctor} - {self.day}: {self.start_time}-{self.end_time}"

class BlacklistedToken(models.Model):
    """
    Store blacklisted refresh tokens for logout functionality
    """
    token = models.CharField(max_length=500, unique=True)
    blacklisted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Blacklisted token at {self.blacklisted_at}"
