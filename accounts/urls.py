# accounts/urls.py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # api/auth/register/patient/ - Changed to match spec: patient/signup
    path('patient/signup/', views.PatientRegistrationView.as_view(), name='register-patient'),
    
    # api/auth/register/doctor/
    path('register/doctor/', views.DoctorRegistrationView.as_view(), name='register-doctor'),
    
    # api/auth/register/pharmacy/
    path('register/pharmacy/', views.PharmacyRegistrationView.as_view(), name='register-pharmacy'),
    
    # api/auth/register/lab/
    path('register/lab/', views.LabRegistrationView.as_view(), name='register-lab'),
    
    # api/auth/register/radiology/
    path('register/radiology/', views.RadiologyRegistrationView.as_view(), name='register-radiology'),

    # Login endpoint (all roles)
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Refresh token endpoint
    path('refresh/', views.RefreshTokenView.as_view(), name='auth-refresh'),
    
    # Logout endpoint
    path('logout/', views.LogoutView.as_view(), name='auth-logout'),

    # GET/PATCH/PUT api/auth/me/
    path('me/', views.UserProfileView.as_view(), name='user-profile'),
]