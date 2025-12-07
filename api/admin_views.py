# api/admin_views.py
"""
Admin views for managing doctors, pharmacies, laboratories, radiologies, and reservations
"""
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from accounts.models import (User, DoctorProfile, PharmacyProfile, 
                              LaboratoryProfile, RadiologyProfile,
                              WorkingHours, DoctorAvailability)
from accounts.serializers import (DoctorCreateSerializer, PharmacyCreateSerializer,
                                   LaboratoryCreateSerializer, RadiologyCreateSerializer,
                                   WorkingHoursSerializer, DoctorAvailabilitySerializer)
from appointments.models import Appointment
from appointments.serializers import AppointmentListSerializer
from .permissions import IsAdmin


class CreateAdminView(APIView):
    """
    POST /admin/create-admin
    Create a new admin user (super admin only)
    """
    permission_classes = [IsAdmin]
    
    def post(self, request):
        # Check if user is superuser
        if not request.user.is_superuser:
            return Response(
                {"success": False, "error": "Only super admins can create admin users"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not all([first_name, last_name, email, password]):
            return Response(
                {"success": False, "error": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return Response(
                {"success": False, "error": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create admin user
        username = email.split('@')[0]
        user = User.objects.create(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password),
            role=User.Role.ADMIN,
            is_approved=True,
            is_staff=True
        )
        
        return Response({
            "success": True,
            "id": str(user.id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        }, status=status.HTTP_201_CREATED)


class AdminDoctorListCreateView(generics.ListCreateAPIView):
    """
    GET/POST /admin/doctors
    List all doctors (with filters) or create a new doctor
    """
    serializer_class = DoctorCreateSerializer
    permission_classes = [IsAdmin]
    
    def get_queryset(self):
        queryset = User.objects.filter(role=User.Role.DOCTOR).select_related('doctor_profile')
        
        # Filters
        specialization = self.request.query_params.get('specialization')
        name = self.request.query_params.get('name')
        
        if specialization:
            queryset = queryset.filter(doctor_profile__specialization__name__icontains=specialization)
        
        if name:
            queryset = queryset.filter(
                first_name__icontains=name
            ) | queryset.filter(
                last_name__icontains=name
            )
        
        return queryset


class AdminDoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET/PUT/DELETE /admin/doctors/{doctorId}
    Retrieve, update, or delete a specific doctor
    """
    serializer_class = DoctorCreateSerializer
    permission_classes = [IsAdmin]
    queryset = User.objects.filter(role=User.Role.DOCTOR)
    lookup_field = 'id'
    lookup_url_kwarg = 'doctorId'
    
    def perform_destroy(self, instance):
        # Soft delete by setting is_approved to False
        instance.is_approved = False
        instance.is_active = False
        instance.save()


class AdminPharmacyCreateView(generics.CreateAPIView):
    """
    POST /admin/pharmacies
    Create a new pharmacy
    """
    serializer_class = PharmacyCreateSerializer
    permission_classes = [IsAdmin]


class AdminLaboratoryCreateView(generics.CreateAPIView):
    """
    POST /admin/laboratories
    Create a new laboratory
    """
    serializer_class = LaboratoryCreateSerializer
    permission_classes = [IsAdmin]


class AdminRadiologyCreateView(generics.CreateAPIView):
    """
    POST /admin/radiologies
    Create a new radiology center
    """
    serializer_class = RadiologyCreateSerializer
    permission_classes = [IsAdmin]


class AdminReservationListView(generics.ListAPIView):
    """
    GET /admin/reservations
    List all reservations with optional filters
    """
    serializer_class = AppointmentListSerializer
    permission_classes = [IsAdmin]
    
    def get_queryset(self):
        queryset = Appointment.objects.all().select_related('patient', 'doctor')
        
        # Filters
        doctor_id = self.request.query_params.get('doctor_id')
        patient_id = self.request.query_params.get('patient_id')
        status_filter = self.request.query_params.get('status')
        
        if doctor_id:
            queryset = queryset.filter(doctor__user_id=doctor_id)
        
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset


class WorkingHoursView(APIView):
    """
    GET/PUT /{ownerType}/{ownerId}/working-hours
    Get or set working hours for pharmacy/laboratory/radiology
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, ownerType, ownerId):
        """Get working hours for an owner"""
        working_hours = WorkingHours.objects.filter(
            owner_type=ownerType,
            owner_id=ownerId
        )
        
        serializer = WorkingHoursSerializer(working_hours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, ownerType, ownerId):
        """Set/update working hours for an owner (admin or owner)"""
        # Check if user is admin or the owner
        user = request.user
        is_owner = False
        
        if ownerType == 'pharmacy' and user.role == User.Role.PHARMACY:
            is_owner = user.id == int(ownerId)
        elif ownerType == 'laboratory' and user.role == User.Role.LAB:
            is_owner = user.id == int(ownerId)
        elif ownerType == 'radiology' and user.role == User.Role.RADIOLOGY:
            is_owner = user.id == int(ownerId)
        
        is_admin = user.role == User.Role.ADMIN or user.is_staff
        
        if not (is_admin or is_owner):
            return Response(
                {"error": "Permission denied"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Delete existing working hours
        WorkingHours.objects.filter(
            owner_type=ownerType,
            owner_id=ownerId
        ).delete()
        
        # Create new working hours
        working_hours_data = request.data
        if not isinstance(working_hours_data, list):
            return Response(
                {"error": "Expected a list of working hours"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        created_hours = []
        for item in working_hours_data:
            item['owner_type'] = ownerType
            item['owner_id'] = ownerId
            serializer = WorkingHoursSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                created_hours.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(created_hours, status=status.HTTP_200_OK)


class DoctorAvailabilityView(APIView):
    """
    POST /admin/doctors/{doctorId}/availabilities
    Add availability entries for a doctor
    """
    permission_classes = [IsAdmin]
    
    def post(self, request, doctorId):
        """Add availability slots for a doctor"""
        try:
            doctor = DoctorProfile.objects.get(user_id=doctorId)
        except DoctorProfile.DoesNotExist:
            return Response(
                {"error": "Doctor not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        availabilities_data = request.data
        if not isinstance(availabilities_data, list):
            return Response(
                {"error": "Expected a list of availability entries"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        created_availabilities = []
        for item in availabilities_data:
            # Check for overlaps
            day = item.get('day')
            start_time = item.get('start_time')
            end_time = item.get('end_time')
            
            # Simple overlap check
            overlapping = DoctorAvailability.objects.filter(
                doctor=doctor,
                day=day,
                start_time__lt=end_time,
                end_time__gt=start_time
            ).exists()
            
            if overlapping:
                return Response(
                    {"error": f"Overlapping availability on {day}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer = DoctorAvailabilitySerializer(data=item)
            if serializer.is_valid():
                serializer.save(doctor=doctor)
                created_availabilities.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(created_availabilities, status=status.HTTP_201_CREATED)
