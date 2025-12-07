# 🏥 Vezeeta-Style Medical Platform API - Complete Summary

## 📋 Overview
This is a comprehensive backend API for a medical platform similar to Vezeeta, built with Django REST Framework. It supports multiple user roles and provides complete CRUD operations for managing doctors, pharmacies, laboratories, radiology centers, and patient reservations.

---

## 🔑 Authentication System

### Endpoints

#### 1. Patient Signup
```
POST /api/auth/patient/signup/
```
**Body:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "password": "secure123",
  "phone": "+1234567890",
  "date_of_birth": "1990-01-01",
  "gender": "male"
}
```

#### 2. Login (All Roles)
```
POST /api/auth/login/
```
**Body:**
```json
{
  "username": "email@example.com",
  "password": "password123"
}
```
**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### 3. Refresh Token
```
POST /api/auth/refresh/
```
**Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```
**Response:**
```json
{
  "success": true,
  "access_token": "new_access_token",
  "expires_in": 3600
}
```

#### 4. Logout
```
POST /api/auth/logout/
```
**Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### 5. Get/Update Profile
```
GET/PATCH/PUT /api/auth/me/
Authorization: Bearer <access_token>
```

---

## 👨‍💼 Admin Endpoints

### 1. Create Admin User
```
POST /api/admin/create-admin/
Authorization: Bearer <super_admin_token>
```
**Body:**
```json
{
  "first_name": "Admin",
  "last_name": "User",
  "email": "admin@example.com",
  "password": "admin123"
}
```

### 2. Manage Doctors

#### List/Create Doctors
```
GET/POST /api/admin/doctors/
Authorization: Bearer <admin_token>
```

**GET Query Parameters:**
- `specialization`: Filter by specialization
- `name`: Filter by doctor name
- `page`: Pagination page number
- `limit`: Results per page

**POST Body:**
```json
{
  "first_name": "Ahmed",
  "last_name": "Hassan",
  "email": "doctor@example.com",
  "password": "doctor123",
  "phone": "+1234567890",
  "address": "123 Medical St",
  "specialization_name": "Cardiology",
  "experience": 5,
  "fee": 150.00,
  "description": "Experienced cardiologist",
  "license_number": "LIC123456"
}
```

#### Get/Update/Delete Doctor
```
GET/PUT/DELETE /api/admin/doctors/{doctorId}/
Authorization: Bearer <admin_token>
```

### 3. Create Pharmacy
```
POST /api/admin/pharmacies/
Authorization: Bearer <admin_token>
```
**Body:**
```json
{
  "name": "City Pharmacy",
  "email": "pharmacy@example.com",
  "password": "pharmacy123",
  "phone": "+1234567890",
  "address": "456 Health Ave",
  "license_number": "PHARM789",
  "working_hours": [
    {
      "day": "Saturday",
      "open_time": "08:00",
      "close_time": "22:00"
    }
  ]
}
```

### 4. Create Laboratory
```
POST /api/admin/laboratories/
Authorization: Bearer <admin_token>
```

### 5. Create Radiology Center
```
POST /api/admin/radiologies/
Authorization: Bearer <admin_token>
```

### 6. List All Reservations
```
GET /api/admin/reservations/
Authorization: Bearer <admin_token>
```
**Query Parameters:**
- `doctor_id`: Filter by doctor
- `patient_id`: Filter by patient
- `status`: Filter by status (pending, confirmed, canceled, completed)

### 7. Add Doctor Availabilities
```
POST /api/admin/doctors/{doctorId}/availabilities/
Authorization: Bearer <admin_token>
```
**Body:**
```json
[
  {
    "day": "Saturday",
    "start_time": "09:00",
    "end_time": "17:00"
  },
  {
    "day": "Sunday",
    "start_time": "09:00",
    "end_time": "14:00"
  }
]
```

---

## 🏥 Working Hours Management

### Get/Set Working Hours
```
GET/PUT /api/{ownerType}/{ownerId}/working-hours/
Authorization: Bearer <token>
```

**ownerType:** `pharmacy`, `laboratory`, or `radiology`

**PUT Body:**
```json
[
  {
    "day": "Saturday",
    "open_time": "08:00",
    "close_time": "22:00"
  },
  {
    "day": "Sunday",
    "open_time": "09:00",
    "close_time": "20:00"
  }
]
```

---

## 👨‍⚕️ Doctor Endpoints

### Get Doctor Profile & Reservations
```
GET /api/doctor/profile/
GET /api/doctor/reservations/
Authorization: Bearer <doctor_token>
```

**Query Parameters for reservations:**
- `date`: Filter by specific date (YYYY-MM-DD)

---

## 🧪 Public Endpoints

### 1. List Doctors
```
GET /api/doctors/
```

### 2. List Pharmacies
```
GET /api/pharmacies/
GET /api/pharmacies/{id}/
```

### 3. List Laboratories
```
GET /api/laboratories/
GET /api/laboratories/{id}/
```

### 4. List Radiology Centers
```
GET /api/radiologies/
```

---

## 🤒 Patient Endpoints

### 1. Create/List Reservations
```
GET/POST /api/patient/reservations/
Authorization: Bearer <patient_token>
```

**POST Body:**
```json
{
  "doctor_id": 5,
  "date": "2025-12-15",
  "time": "10:00"
}
```

### 2. Cancel Reservation
```
PUT /api/patient/reservations/{id}/cancel/
Authorization: Bearer <patient_token>
```

---

## 📊 Database Models

### User Roles
- `patient` - Regular patients
- `doctor` - Medical doctors
- `pharmacy` - Pharmacy owners
- `laboratory` - Laboratory owners
- `radiology` - Radiology center owners
- `admin` - System administrators

### Key Models
1. **User** - Base user with role-based authentication
2. **PatientProfile** - Extended patient information
3. **DoctorProfile** - Doctor details with specialization, fee, experience
4. **PharmacyProfile** - Pharmacy information
5. **LaboratoryProfile** - Lab details
6. **RadiologyProfile** - Radiology center details
7. **WorkingHours** - Operating hours for facilities
8. **DoctorAvailability** - Doctor availability slots
9. **Appointment (Reservation)** - Patient reservations
10. **BlacklistedToken** - Logout token management

---

## 🔐 Security Features

1. **JWT Authentication** - Secure token-based auth
2. **Refresh Token System** - Long-lived refresh tokens
3. **Token Blacklisting** - Secure logout mechanism
4. **Role-Based Access Control** - Granular permissions
5. **Approval System** - Admin approval required for providers

---

## 🚀 Getting Started

### Installation

```bash
# Clone repository
git clone <repository-url>
cd webapp

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

### Default Admin Credentials
```
Username: admin
Email: admin@example.com
Password: admin123
```

---

## 📝 API Response Format

### Success Response
```json
{
  "success": true,
  "data": { },
  "message": "Operation successful"
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message",
  "details": { }
}
```

---

## 🎯 Key Features

✅ Multi-role user system (6 roles)  
✅ Complete CRUD for all entities  
✅ JWT with refresh token support  
✅ Token blacklisting for logout  
✅ Admin approval system  
✅ Working hours management  
✅ Doctor availability system  
✅ Reservation management  
✅ Role-based permissions  
✅ Filtering and pagination  
✅ Comprehensive API documentation  

---

## 📞 Support

For issues or questions, please refer to the API documentation or contact the development team.
