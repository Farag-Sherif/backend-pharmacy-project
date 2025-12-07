# appointments/serializers.py
from rest_framework import serializers
from .models import Appointment
from accounts.models import User, DoctorProfile, LaboratoryProfile
from accounts.serializers import PatientProfileSerializer

class AppointmentCreateSerializer(serializers.ModelSerializer):
    doctor_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Appointment
        fields = ('doctor_id', 'date', 'time', 'notes_from_patient')
    
    def validate(self, data):
        if not data.get('doctor_id'):
            raise serializers.ValidationError("doctor_id is required.")
        
        # Check if doctor exists
        try:
            doctor = DoctorProfile.objects.get(user_id=data['doctor_id'])
        except DoctorProfile.DoesNotExist:
            raise serializers.ValidationError("Doctor not found.")
        
        data['doctor'] = doctor
        data.pop('doctor_id')
        
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
    doctor_id = serializers.IntegerField(source='doctor.user_id', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'patient_id', 'doctor_id', 'date', 'time', 'status', 'notes_from_patient')

class AppointmentManageSerializer(serializers.ModelSerializer):
    
    status = serializers.ChoiceField(
        choices=[
            Appointment.Status.CONFIRMED, 
            Appointment.Status.CANCELED,
            Appointment.Status.COMPLETED
        ]
    )
    
    class Meta:
        model = Appointment
        fields = ('status', 'notes_from_provider')
        read_only_fields = ('patient', 'doctor', 'date', 'time', 'notes_from_patient')