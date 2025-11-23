# api/permissions.py
from rest_framework.permissions import BasePermission
from accounts.models import User

class IsPatient(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == User.Role.PATIENT
        )

class IsDoctor(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == User.Role.DOCTOR
        )

class IsLab(BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == User.Role.LAB
        )
    
class IsAppointmentOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == User.Role.DOCTOR and hasattr(user, 'doctor_profile'):
            return obj.doctor == user.doctor_profile
            
        if user.role == User.Role.LAB and hasattr(user, 'lab_profile'):
            return obj.laboratory == user.lab_profile
            
        return False
    
class IsPharmacy(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == User.Role.PHARMACY
        )