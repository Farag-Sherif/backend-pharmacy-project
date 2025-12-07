# 🧪 API Testing Guide

## Quick Start Testing

### 1. Run the Development Server

```bash
cd /home/user/webapp
python manage.py runserver
```

The server will be available at: `http://127.0.0.1:8000/`

---

## 🔐 Authentication Flow

### Step 1: Login as Admin
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

**Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

Save the `access` token for subsequent requests.

---

## 👨‍⚕️ Testing Doctor Management

### Create a Doctor (Admin)
```bash
curl -X POST http://127.0.0.1:8000/api/admin/doctors/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Ahmed",
    "last_name": "Hassan",
    "email": "ahmed.hassan@example.com",
    "password": "doctor123",
    "phone": "+201234567890",
    "address": "123 Medical Street, Cairo",
    "specialization_name": "Cardiology",
    "experience": 10,
    "fee": 200.00,
    "description": "Experienced cardiologist with 10 years of practice",
    "license_number": "DOC123456"
  }'
```

### List All Doctors (Admin)
```bash
curl -X GET http://127.0.0.1:8000/api/admin/doctors/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Filter Doctors by Specialization
```bash
curl -X GET "http://127.0.0.1:8000/api/admin/doctors/?specialization=Cardiology" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Update Doctor
```bash
curl -X PUT http://127.0.0.1:8000/api/admin/doctors/2/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Ahmed",
    "last_name": "Hassan",
    "fee": 250.00,
    "experience": 11
  }'
```

### Approve Doctor (via Django Admin)
1. Go to: http://127.0.0.1:8000/admin/
2. Login with admin credentials
3. Go to Users > Find the doctor
4. Check "Is approved" and save

---

## 🏥 Testing Pharmacy Management

### Create a Pharmacy (Admin)
```bash
curl -X POST http://127.0.0.1:8000/api/admin/pharmacies/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "City Pharmacy",
    "email": "city.pharmacy@example.com",
    "password": "pharmacy123",
    "phone": "+201234567891",
    "address": "456 Health Avenue, Cairo",
    "license_number": "PHARM789"
  }'
```

### Set Working Hours for Pharmacy
```bash
curl -X PUT http://127.0.0.1:8000/api/pharmacy/3/working-hours/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "day": "Saturday",
      "open_time": "08:00",
      "close_time": "22:00"
    },
    {
      "day": "Sunday",
      "open_time": "08:00",
      "close_time": "22:00"
    },
    {
      "day": "Monday",
      "open_time": "08:00",
      "close_time": "20:00"
    }
  ]'
```

### Get Working Hours
```bash
curl -X GET http://127.0.0.1:8000/api/pharmacy/3/working-hours/
```

---

## 🧪 Testing Laboratory & Radiology

### Create Laboratory
```bash
curl -X POST http://127.0.0.1:8000/api/admin/laboratories/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Central Lab",
    "email": "central.lab@example.com",
    "password": "lab123",
    "phone": "+201234567892",
    "address": "789 Science Road, Cairo",
    "license_number": "LAB456"
  }'
```

### Create Radiology Center
```bash
curl -X POST http://127.0.0.1:8000/api/admin/radiologies/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Modern Radiology Center",
    "email": "radiology@example.com",
    "password": "rad123",
    "phone": "+201234567893",
    "address": "321 Imaging Street, Cairo",
    "license_number": "RAD789"
  }'
```

---

## 📅 Testing Doctor Availability

### Add Doctor Availabilities
```bash
curl -X POST http://127.0.0.1:8000/api/admin/doctors/2/availabilities/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "day": "Saturday",
      "start_time": "09:00",
      "end_time": "17:00"
    },
    {
      "day": "Sunday",
      "start_time": "09:00",
      "end_time": "14:00"
    },
    {
      "day": "Monday",
      "start_time": "09:00",
      "end_time": "17:00"
    }
  ]'
```

---

## 🤒 Testing Patient Flow

### Step 1: Register as Patient
```bash
curl -X POST http://127.0.0.1:8000/api/auth/patient/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Mohamed",
    "last_name": "Ali",
    "email": "mohamed.ali@example.com",
    "password": "patient123",
    "phone": "+201234567894",
    "date_of_birth": "1990-05-15",
    "gender": "male"
  }'
```

### Step 2: Login as Patient
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "mohamed.ali@example.com",
    "password": "patient123"
  }'
```

### Step 3: Browse Approved Doctors
```bash
curl -X GET http://127.0.0.1:8000/api/doctors/ \
  -H "Authorization: Bearer PATIENT_ACCESS_TOKEN"
```

### Step 4: Create a Reservation
```bash
curl -X POST http://127.0.0.1:8000/api/patient/reservations/ \
  -H "Authorization: Bearer PATIENT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "doctor_id": 2,
    "date": "2025-12-20",
    "time": "10:00"
  }'
```

### Step 5: List My Reservations
```bash
curl -X GET http://127.0.0.1:8000/api/patient/reservations/ \
  -H "Authorization: Bearer PATIENT_ACCESS_TOKEN"
```

### Step 6: Cancel a Reservation
```bash
curl -X PUT http://127.0.0.1:8000/api/patient/reservations/1/cancel/ \
  -H "Authorization: Bearer PATIENT_ACCESS_TOKEN"
```

---

## 🔄 Testing Token Refresh

### Refresh Access Token
```bash
curl -X POST http://127.0.0.1:8000/api/auth/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "YOUR_REFRESH_TOKEN"
  }'
```

### Logout
```bash
curl -X POST http://127.0.0.1:8000/api/auth/logout/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "YOUR_REFRESH_TOKEN"
  }'
```

---

## 📊 Testing Admin Features

### View All Reservations
```bash
curl -X GET http://127.0.0.1:8000/api/admin/reservations/ \
  -H "Authorization: Bearer ADMIN_ACCESS_TOKEN"
```

### Filter Reservations by Doctor
```bash
curl -X GET "http://127.0.0.1:8000/api/admin/reservations/?doctor_id=2" \
  -H "Authorization: Bearer ADMIN_ACCESS_TOKEN"
```

### Filter by Status
```bash
curl -X GET "http://127.0.0.1:8000/api/admin/reservations/?status=pending" \
  -H "Authorization: Bearer ADMIN_ACCESS_TOKEN"
```

---

## 🧪 Using Postman

### Import Collection
1. Create a new collection in Postman
2. Add environment variables:
   - `base_url`: http://127.0.0.1:8000
   - `access_token`: (will be set after login)
   - `refresh_token`: (will be set after login)

### Example Request in Postman
```
Method: POST
URL: {{base_url}}/api/auth/login/
Headers:
  Content-Type: application/json
Body (raw JSON):
{
  "username": "admin",
  "password": "admin123"
}
```

### Set Tokens Automatically (Tests tab)
```javascript
var jsonData = pm.response.json();
pm.environment.set("access_token", jsonData.access);
pm.environment.set("refresh_token", jsonData.refresh);
```

---

## 🐛 Common Issues & Solutions

### Issue: "Token is invalid or expired"
**Solution:** Refresh your access token using the refresh endpoint

### Issue: "User is not approved"
**Solution:** Login to Django admin and approve the user

### Issue: "Permission denied"
**Solution:** Ensure you're using the correct role's token

### Issue: "Doctor not found"
**Solution:** Create a doctor first or use an existing doctor_id

---

## 📝 Test Checklist

- [ ] Admin can create admins
- [ ] Admin can create/update/delete doctors
- [ ] Admin can create pharmacies/labs/radiologies
- [ ] Admin can view all reservations
- [ ] Admin can add doctor availabilities
- [ ] Patient can register and login
- [ ] Patient can browse approved doctors
- [ ] Patient can create reservations
- [ ] Patient can cancel reservations
- [ ] Patient can view their reservations
- [ ] Doctor can view their schedule
- [ ] Pharmacy can manage working hours
- [ ] Token refresh works correctly
- [ ] Logout blacklists tokens
- [ ] Role-based permissions work

---

## 🚀 Production Testing

For production environments, replace `http://127.0.0.1:8000` with your production API URL.

Example:
```bash
export API_URL="https://api.example.com"
curl -X POST $API_URL/api/auth/login/ ...
```
