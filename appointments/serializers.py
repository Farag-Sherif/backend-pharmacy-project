# appointments/serializers.py
from rest_framework import serializers
from .models import Appointment
from accounts.models import User, DoctorProfile, LaboratoryProfile
from accounts.serializers import PatientProfileSerializer

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('doctor', 'laboratory', 'appointment_time', 'notes_from_patient')

    def validate(self, data):
        
        if data.get('doctor') and data.get('laboratory'):
            raise serializers.ValidationError("لا يمكن اختيار طبيب ومعمل في نفس الحجز.")
        
        if not data.get('doctor') and not data.get('laboratory'):
            raise serializers.ValidationError("يجب اختيار طبيب أو معمل.")
            
        
        return data

class PatientForAppointmentSerializer(serializers.ModelSerializer):
    
    patient_profile = PatientProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'patient_profile' 
        )  


class AppointmentListSerializer(serializers.ModelSerializer):
    patient = PatientForAppointmentSerializer(read_only=True)
    
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'appointment_time', 'status', 'notes_from_patient')

class AppointmentManageSerializer(serializers.ModelSerializer):
    
    
    status = serializers.ChoiceField(
        choices=[
            Appointment.Status.APPROVED, 
            Appointment.Status.REJECTED,
            Appointment.Status.COMPLETED
        ]
    )
    
    class Meta:
        model = Appointment
        fields = ('status', 'notes_from_provider')
        read_only_fields = ('patient', 'doctor', 'laboratory', 'appointment_time', 'notes_from_patient')