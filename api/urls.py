# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # /api/doctors/
    path('doctors/', views.DoctorListView.as_view(), name='doctor-list'),
    path('appointments/book/', views.AppointmentCreateView.as_view(), name='book-appointment'),
    path('doctors/my-appointments/', views.DoctorAppointmentListView.as_view(), name='doctor-appointments'),
    path('labs/my-appointments/', views.LabAppointmentListView.as_view(), name='lab-appointments'),
    path(
        'appointments/<int:pk>/manage/', 
        views.AppointmentManageView.as_view(), 
        name='manage-appointment'
    ),
    path(
        'pharmacies/', 
        views.PharmacyListView.as_view(), 
        name='pharmacy-list'
    ),
    path(
        'pharmacies/<int:pk>/', 
        views.PharmacyDetailView.as_view(), 
        name='pharmacy-detail'
    ),
    path(
        'pharmacies/my-medicines/', 
        views.PharmacyMedicineManageView.as_view(), 
        name='pharmacy-medicines'
    ),
    path(
        'pharmacies/my-medicines/<int:pk>/', 
        views.PharmacyMedicineDetailView.as_view(), 
        name='pharmacy-medicine-detail'
    ),
    path(
        'pharmacies/my-medicines/', 
        views.PharmacyMedicineManageView.as_view(), 
        name='pharmacy-medicines'
    ),
    path(
        'pharmacies/my-medicines/<int:pk>/', 
        views.PharmacyMedicineDetailView.as_view(), 
        name='pharmacy-medicine-detail'
    ),

    path('labs/', views.LaboratoryListView.as_view(), name='lab-list'),
    path('labs/<int:pk>/', views.LaboratoryDetailView.as_view(), name='lab-detail'),
    path('labs/my-appointments/', views.LabAppointmentListView.as_view(), name='lab-appointments'),

]