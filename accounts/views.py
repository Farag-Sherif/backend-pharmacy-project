from django.shortcuts import render
# accounts/views.py
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, BlacklistedToken
from .serializers import RegistrationSerializer, UserProfileSerializer
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

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

class RadiologyRegistrationView(generics.CreateAPIView):
   
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        return {
            'request': self.request,
            'view': self,
            'role': User.Role.RADIOLOGY,
            'is_approved': False 
        }

class CustomTokenObtainPairView(TokenObtainPairView):
   
    serializer_class = CustomTokenObtainPairSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    
    serializer_class = UserProfileSerializer
    
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class RefreshTokenView(APIView):
    """
    Refresh access token using refresh token
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        
        if not refresh_token:
            return Response(
                {"success": False, "error": "refresh_token is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if token is blacklisted
        if BlacklistedToken.objects.filter(token=refresh_token).exists():
            return Response(
                {"success": False, "error": "Token has been revoked"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            
            return Response({
                "success": True,
                "access_token": access_token,
                "expires_in": 3600  # 1 hour in seconds
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"success": False, "error": "Invalid or expired refresh token"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )

class LogoutView(APIView):
    """
    Logout by blacklisting the refresh token
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        
        if not refresh_token:
            return Response(
                {"success": False, "error": "refresh_token is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Add token to blacklist
        BlacklistedToken.objects.get_or_create(token=refresh_token)
        
        return Response({
            "success": True,
            "message": "Logged out successfully"
        }, status=status.HTTP_200_OK)
