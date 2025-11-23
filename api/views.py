# api/views.py
from django.shortcuts import render
from rest_framework import generics, permissions
from accounts.models import User
from .serializers import DoctorListSerializer
from appointments.models import Appointment
from appointments.serializers import (
    AppointmentCreateSerializer, AppointmentListSerializer
)
from .permissions import IsPatient, IsDoctor, IsLab
from .permissions import IsPatient, IsDoctor, IsLab, IsAppointmentOwner
from appointments.serializers import (
    AppointmentCreateSerializer, AppointmentListSerializer, AppointmentManageSerializer
)
from pharmacy.models import Medicine
from pharmacy.serializers import MedicineSerializer
from .permissions import IsPharmacy
from rest_framework import permissions
from .serializers import (
    PharmacyListSerializer, PharmacyDetailSerializer
)
from .serializers import (
    LaboratoryListSerializer, LaboratoryDetailSerializer
)

class DoctorListView(generics.ListAPIView):
    
    
    queryset = User.objects.filter(
        role=User.Role.DOCTOR, 
        is_approved=True
    ).select_related('doctor_profile', 'doctor_profile__specialization')
    
    serializer_class = DoctorListSerializer
    
    permission_classes = [permissions.IsAuthenticated]

class AppointmentCreateView(generics.CreateAPIView):
    
    serializer_class = AppointmentCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsPatient]

    def perform_create(self, serializer):
        serializer.save(
            patient=self.request.user,
            status=Appointment.Status.PENDING 
        )

class DoctorAppointmentListView(generics.ListAPIView):
    
    serializer_class = AppointmentListSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return Appointment.objects.filter(
            doctor=self.request.user.doctor_profile
        ).select_related('patient').order_by('appointment_time')

class LabAppointmentListView(generics.ListAPIView):
    
    serializer_class = AppointmentListSerializer
    permission_classes = [permissions.IsAuthenticated, IsLab]

    def get_queryset(self):
        return Appointment.objects.filter(
            laboratory=self.request.user.lab_profile
        ).select_related('patient').order_by('appointment_time')
    
class AppointmentManageView(generics.RetrieveUpdateAPIView):
   
    serializer_class = AppointmentManageSerializer
    queryset = Appointment.objects.all() 
    
    permission_classes = [
        permissions.IsAuthenticated, 
        IsAppointmentOwner           
    ]


class PharmacyMedicineManageView(generics.ListCreateAPIView):
   
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated, IsPharmacy]

    def get_queryset(self):
        return Medicine.objects.filter(
            pharmacy=self.request.user.pharmacy_profile
        )

    def perform_create(self, serializer):
        serializer.save(pharmacy=self.request.user.pharmacy_profile)

class PharmacyMedicineDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated, IsPharmacy]

    def get_queryset(self):
        return Medicine.objects.filter(
            pharmacy=self.request.user.pharmacy_profile
        )
    
class PharmacyListView(generics.ListAPIView):
   
    queryset = User.objects.filter(
        role=User.Role.PHARMACY,
        is_approved=True
    ).select_related('pharmacy_profile')
    
    serializer_class = PharmacyListSerializer
    permission_classes = [permissions.IsAuthenticated]

class PharmacyDetailView(generics.RetrieveAPIView):
   
    queryset = User.objects.filter(
        role=User.Role.PHARMACY,
        is_approved=True
    ).select_related('pharmacy_profile')
    
    serializer_class = PharmacyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class LaboratoryListView(generics.ListAPIView):
    
    queryset = User.objects.filter(
        role=User.Role.LAB,
        is_approved=True
    ).select_related('lab_profile')
    
    serializer_class = LaboratoryListSerializer
    permission_classes = [permissions.IsAuthenticated]

class LaboratoryDetailView(generics.RetrieveAPIView):
    
    queryset = User.objects.filter(
        role=User.Role.LAB,
        is_approved=True
    ).select_related('lab_profile')
    
    serializer_class = LaboratoryDetailSerializer
    permission_classes = [permissions.IsAuthenticated]