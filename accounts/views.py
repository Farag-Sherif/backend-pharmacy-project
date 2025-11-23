from django.shortcuts import render
# accounts/views.py
from rest_framework import generics, permissions
from .models import User
from .serializers import RegistrationSerializer, UserProfileSerializer
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class PatientRegistrationView(generics.CreateAPIView):
   
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {
            'request': self.request,
            # 'format': self.format_json,
            'view': self,
            'role': User.Role.PATIENT,
            'is_approved': True  
        }

class DoctorRegistrationView(generics.CreateAPIView):
   
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {
            'request': self.request,
            # 'format': self.format_json,
            'view': self,
            'role': User.Role.DOCTOR,
            'is_approved': False 
        }

class PharmacyRegistrationView(generics.CreateAPIView):

    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {
            'request': self.request,
            # 'format': self.format_json,
            'view': self,
            'role': User.Role.PHARMACY,
            'is_approved': False 
        }

class LabRegistrationView(generics.CreateAPIView):
   
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {
            'request': self.request,
            # 'format': self.format_json,
            'view': self,
            'role': User.Role.LAB,
            'is_approved': False 
        }
class CustomTokenObtainPairView(TokenObtainPairView):
   
    serializer_class = CustomTokenObtainPairSerializer

class UserProfileView(generics.RetrieveAPIView):
    
    serializer_class = UserProfileSerializer
    
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
