# pharmacy/serializers.py
from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ('id', 'name', 'description', 'price', 'in_stock', 'pharmacy')
        read_only_fields = ('pharmacy',)