# api/urls.py
from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    # =============== ADMIN ENDPOINTS ===============
    # Admin - Create Admin
    path('admin/create-admin/', admin_views.CreateAdminView.as_view(), name='admin-create-admin'),
    
    # Admin - Doctors CRUD
    path('admin/doctors/', admin_views.AdminDoctorListCreateView.as_view(), name='admin-doctors'),
    path('admin/doctors/<int:doctorId>/', admin_views.AdminDoctorDetailView.as_view(), name='admin-doctor-detail'),
    
    # Admin - Pharmacies
    path('admin/pharmacies/', admin_views.AdminPharmacyCreateView.as_view(), name='admin-pharmacies'),
    
    # Admin - Laboratories
    path('admin/laboratories/', admin_views.AdminLaboratoryCreateView.as_view(), name='admin-laboratories'),
    
    # Admin - Radiologies
    path('admin/radiologies/', admin_views.AdminRadiologyCreateView.as_view(), name='admin-radiologies'),
    
    # Admin - Reservations
    path('admin/reservations/', admin_views.AdminReservationListView.as_view(), name='admin-reservations'),
    
    # Admin - Doctor Availabilities
    path('admin/doctors/<int:doctorId>/availabilities/', admin_views.DoctorAvailabilityView.as_view(), name='admin-doctor-availabilities'),
    
    # Working Hours (for pharmacy/lab/radiology)
    path('<str:ownerType>/<int:ownerId>/working-hours/', admin_views.WorkingHoursView.as_view(), name='working-hours'),
    
    # =============== PUBLIC/PATIENT ENDPOINTS ===============
    # Public - Doctors List
    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
    
    # Public - Pharmacies
    path('pharmacies/', views.PharmacyListView.as_view(), name='pharmacy-list'),
    path('pharmacies/<int:pk>/', views.PharmacyDetailView.as_view(), name='pharmacy-detail'),
    
    # Public - Laboratories
    path('laboratories/', views.LaboratoryListView.as_view(), name='lab-list'),
    path('laboratories/<int:pk>/', views.LaboratoryDetailView.as_view(), name='lab-detail'),
    
    # Public - Radiologies
    path('radiologies/', views.RadiologyListView.as_view(), name='radiology-list'),
    
    # =============== PATIENT ENDPOINTS ===============
    # Patient - Reservations
    path('patient/reservations/', views.AppointmentCreateView.as_view(), name='patient-reservations'),
    path('patient/reservations/<int:pk>/cancel/', views.ReservationCancelView.as_view(), name='patient-reservation-cancel'),
    
    # =============== DOCTOR ENDPOINTS ===============
    # Doctor - Profile
    path('doctor/profile/', views.DoctorAppointmentListView.as_view(), name='doctor-profile'),
    
    # Doctor - Reservations
    path('doctor/reservations/', views.DoctorAppointmentListView.as_view(), name='doctor-reservations'),
    
    # =============== PHARMACY ENDPOINTS ===============
    # Pharmacy - Medicines Management
    path('pharmacies/my-medicines/', views.PharmacyMedicineManageView.as_view(), name='pharmacy-medicines'),
    path('pharmacies/my-medicines/<int:pk>/', views.PharmacyMedicineDetailView.as_view(), name='pharmacy-medicine-detail'),
    
    # =============== LAB ENDPOINTS ===============
    # Lab - Appointments
    path('labs/my-appointments/', views.LabAppointmentListView.as_view(), name='lab-appointments'),
    
    # =============== APPOINTMENT MANAGEMENT ===============
    path('appointments/<int:pk>/manage/', views.AppointmentManageView.as_view(), name='manage-appointment'),
]