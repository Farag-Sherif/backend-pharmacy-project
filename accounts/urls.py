# accounts/urls.py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # api/auth/register/patient/
    path('register/patient/', views.PatientRegistrationView.as_view(), name='register-patient'),
    
    # api/auth/register/doctor/
    path('register/doctor/', views.DoctorRegistrationView.as_view(), name='register-doctor'),
    
    # api/auth/register/pharmacy/
    path('register/pharmacy/', views.PharmacyRegistrationView.as_view(), name='register-pharmacy'),
    
    # api/auth/register/lab/
    path('register/lab/', views.LabRegistrationView.as_view(), name='register-lab'),

     
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # GET/api/auth/me/
    path('me/', views.UserProfileView.as_view(), name='user-profile'),
]