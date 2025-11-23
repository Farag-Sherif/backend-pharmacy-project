# api/serializers.py
from rest_framework import serializers
from accounts.models import User, DoctorProfile, Specialization
from accounts.models import PharmacyProfile
from pharmacy.models import Medicine
from accounts.models import LaboratoryProfile

class SpecializationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Specialization
        fields = ('name',)

class DoctorProfileListSerializer(serializers.ModelSerializer):
   
    specialization = SpecializationSerializer(read_only=True)
    
    class Meta:
        model = DoctorProfile
        fields = ('specialization', 'consultation_fee', 'bio')

class DoctorListSerializer(serializers.ModelSerializer):
    
    doctor_profile = DoctorProfileListSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'profile_picture', 'doctor_profile')

class PharmacyProfileListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PharmacyProfile
        fields = ('address', 'phone_number')

class PharmacyListSerializer(serializers.ModelSerializer):
    
    pharmacy_profile = PharmacyProfileListSerializer(read_only=True)
    
    class Meta:
        model = User 
        fields = ('id', 'username', 'profile_picture', 'pharmacy_profile')



class MedicineListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medicine
        fields = ('id', 'name', 'description', 'price') 

class PharmacyDetailSerializer(serializers.ModelSerializer):
    pharmacy_profile = PharmacyProfileListSerializer(read_only=True)
    
    medicines = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_picture', 'pharmacy_profile', 'medicines')

    def get_medicines(self, obj):
        profile = obj.pharmacy_profile
        available_medicines = profile.medicines.filter(in_stock=True)
        return MedicineListSerializer(available_medicines, many=True).data
    

class LaboratoryProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LaboratoryProfile
        fields = ('address', 'phone_number', 'license_number')

class LaboratoryListSerializer(serializers.ModelSerializer):
    
    lab_profile = LaboratoryProfileSerializer(read_only=True)
    
    class Meta:
        model = User 
        fields = ('id', 'username', 'profile_picture', 'lab_profile')

class LaboratoryDetailSerializer(serializers.ModelSerializer):
    lab_profile = LaboratoryProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'profile_picture', 'lab_profile')