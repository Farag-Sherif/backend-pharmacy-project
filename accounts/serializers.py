# accounts/serializers.py
from rest_framework import serializers
from .models import Specialization, User, PatientProfile, DoctorProfile, PharmacyProfile, LaboratoryProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        role = self.context['role']
        is_approved = self.context['is_approved']

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=role,
            is_approved=is_approved
        )

        if role == User.Role.PATIENT:
            PatientProfile.objects.create(user=user)
        elif role == User.Role.DOCTOR:
            DoctorProfile.objects.create(user=user)
        elif role == User.Role.PHARMACY:
            PharmacyProfile.objects.create(user=user)
        elif role == User.Role.LAB:
            LaboratoryProfile.objects.create(user=user)
        
        return user
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        if not user.is_approved:
            if not user.is_staff and not user.is_superuser:
                raise serializers.ValidationError(
                    "لا يمكن تسجيل الدخول. هذا الحساب غير موافق عليه من قبل الإدارة."
                )

        return data
    
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ('name', 'description')

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ('medical_history', 'date_of_birth')

class DoctorProfileSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True)
    
    class Meta:
        model = DoctorProfile
        fields = ('specialization', 'bio', 'consultation_fee', 'license_number')

class PharmacyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyProfile
        fields = ('address', 'license_number', 'phone_number')

class LaboratoryProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryProfile
        fields = ('address', 'license_number', 'phone_number')



class UserProfileSerializer(serializers.ModelSerializer):
    
    profile_data = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role', 'profile_picture', 'profile_data')

    def get_profile_data(self, obj):
        if obj.role == User.Role.PATIENT and hasattr(obj, 'patient_profile'):
            return PatientProfileSerializer(obj.patient_profile).data
        elif obj.role == User.Role.DOCTOR and hasattr(obj, 'doctor_profile'):
            return DoctorProfileSerializer(obj.doctor_profile).data
        elif obj.role == User.Role.PHARMACY and hasattr(obj, 'pharmacy_profile'):
            return PharmacyProfileSerializer(obj.pharmacy_profile).data
        elif obj.role == User.Role.LAB and hasattr(obj, 'lab_profile'):
            return LaboratoryProfileSerializer(obj.lab_profile).data
        
        return None