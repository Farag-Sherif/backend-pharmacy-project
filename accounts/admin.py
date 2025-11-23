# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Specialization, PatientProfile, 
    DoctorProfile, PharmacyProfile, LaboratoryProfile
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
        (None, {'fields': ('role', 'is_approved')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'is_approved')}),
    )

admin.site.register(Specialization)
admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(PharmacyProfile)
admin.site.register(LaboratoryProfile)