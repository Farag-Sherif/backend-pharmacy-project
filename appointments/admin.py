from django.contrib import admin

# appointments/admin.py
from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'get_provider_name', 'date', 'time', 'status')
    
    list_filter = ('status', 'date', 'doctor')
    
    search_fields = ('patient__username',)
    
    list_editable = ('status',)

    def get_provider_name(self, obj):
        if obj.doctor:
            return str(obj.doctor)
        return "N/A"
    get_provider_name.short_description = 'Provider (Doctor)'
