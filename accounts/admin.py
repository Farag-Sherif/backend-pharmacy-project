# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Specialization, PatientProfile, 
    DoctorProfile, PharmacyProfile, LaboratoryProfile, RadiologyProfile,
    WorkingHours, DoctorAvailability, BlacklistedToken
)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    
    list_display = (
        'username', 'email', 'role', 
        'is_approved', 
        'is_staff'
    )
    
    list_editable = ('is_approved',)
    
    list_filter = ('is_approved', 'role', 'is_staff')
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'is_approved', 'phone', 'profile_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'is_approved')}),
    )

admin.site.register(Specialization)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(PharmacyProfile)
admin.site.register(LaboratoryProfile)
admin.site.register(RadiologyProfile)
admin.site.register(WorkingHours)
admin.site.register(DoctorAvailability)
admin.site.register(BlacklistedToken)