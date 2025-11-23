from django.contrib import admin

# pharmacy/admin.py
from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'pharmacy', 'price', 'in_stock')
    list_filter = ('pharmacy', 'in_stock')
    search_fields = ('name', 'pharmacy__user__username')
    list_editable = ('price', 'in_stock')
