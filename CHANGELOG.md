# Changelog - Vezeeta-Style Medical Platform API

## Version 2.0.0 - Major Update (2025-12-07)

### 🎉 New Features

#### Authentication & Security
- ✅ **Refresh Token System**: Implemented secure token refresh mechanism
- ✅ **Logout Functionality**: Added token blacklisting for secure logout
- ✅ **Enhanced JWT**: Access tokens with 1-hour expiry, refresh tokens with 7-day expiry
- ✅ **Profile Management**: Added GET/PATCH/PUT support for user profiles

#### User Roles & Management
- ✅ **Radiology Role**: New user role for radiology centers
- ✅ **Phone Field**: Added phone number to User model
- ✅ **Gender Field**: Added to PatientProfile (male/female/other)
- ✅ **Address Fields**: Added to all profile types
- ✅ **Experience Field**: Added to DoctorProfile

#### Admin Features
- ✅ **Create Admin Endpoint**: Super admin can create new admin users
- ✅ **Doctor Management**: Full CRUD operations with filtering
  - Create doctors with all fields
  - Update doctor information
  - Soft delete (set is_approved=False)
  - Filter by specialization and name
  - Pagination support
- ✅ **Pharmacy Management**: Create pharmacy accounts
- ✅ **Laboratory Management**: Create laboratory accounts
- ✅ **Radiology Management**: Create radiology center accounts
- ✅ **Reservation Overview**: View all reservations with filters

#### Scheduling System
- ✅ **Working Hours**: Implemented for pharmacies, labs, and radiologies
  - Set operating hours for each day of the week
  - GET/PUT endpoints for management
- ✅ **Doctor Availability**: Schedule management for doctors
  - Define available time slots per day
  - Overlap detection
  - Batch creation of availability slots

#### Reservation System
- ✅ **Separate Date/Time**: Changed from datetime to date + time fields
- ✅ **Status Updates**: Renamed statuses (pending, confirmed, canceled, completed)
- ✅ **Cancel Endpoint**: Patients can cancel their own reservations
- ✅ **List Reservations**: Patients can view their booking history
- ✅ **Admin Filters**: Filter by doctor_id, patient_id, status

### 🔧 Technical Improvements

#### Models
- Created `RadiologyProfile` model
- Created `WorkingHours` model with owner polymorphism
- Created `DoctorAvailability` model
- Created `BlacklistedToken` model
- Updated `Appointment` model (reservation logic)
- Enhanced `User` model with phone field

#### Serializers
- `DoctorCreateSerializer`: For admin doctor management
- `PharmacyCreateSerializer`: For admin pharmacy creation
- `LaboratoryCreateSerializer`: For admin lab creation
- `RadiologyCreateSerializer`: For admin radiology creation
- `WorkingHoursSerializer`: For schedule management
- `DoctorAvailabilitySerializer`: For doctor schedules
- Updated all existing serializers for new fields

#### Views & Endpoints
Created 15+ new API endpoints:
- `/api/admin/create-admin/` - Create admin users
- `/api/admin/doctors/` - List/Create doctors
- `/api/admin/doctors/{id}/` - Get/Update/Delete doctor
- `/api/admin/pharmacies/` - Create pharmacy
- `/api/admin/laboratories/` - Create laboratory
- `/api/admin/radiologies/` - Create radiology
- `/api/admin/reservations/` - List all reservations
- `/api/admin/doctors/{id}/availabilities/` - Manage schedules
- `/api/auth/refresh/` - Refresh access token
- `/api/auth/logout/` - Logout with blacklist
- `/api/patient/reservations/` - List/Create reservations
- `/api/patient/reservations/{id}/cancel/` - Cancel reservation
- `/api/{ownerType}/{ownerId}/working-hours/` - Working hours
- `/api/radiologies/` - Public radiology list

#### Permissions
- Created `IsAdmin` permission class
- Enhanced role-based access control
- Added owner verification for working hours

### 📚 Documentation
- ✅ **API_SUMMARY.md**: Comprehensive API documentation
  - All endpoints documented
  - Request/response examples
  - Authentication flow
  - Setup instructions
- ✅ **TESTING_GUIDE.md**: Complete testing guide
  - cURL examples for all endpoints
  - Postman collection setup
  - Test scenarios
  - Common issues and solutions
- ✅ **CHANGELOG.md**: This file

### 🗃️ Database Changes
- Added 5 new tables
- Modified 3 existing tables
- All migrations created and applied
- Database schema fully tested

### 🔒 Security Enhancements
- Token blacklisting prevents reuse of logout tokens
- Role-based endpoint protection
- Admin approval system maintained
- Password hashing for all user types

### 🧪 Testing
- ✅ All migrations applied successfully
- ✅ Superuser created for testing
- ✅ All endpoints verified
- ✅ Role permissions tested

### 📦 Dependencies Updated
```
django>=4.2,<5.0
djangorestframework>=3.14
djangorestframework-simplejwt>=5.3
django-cors-headers>=4.0
Pillow>=10.0
```

### 🚀 Deployment Notes
- Ensure all migrations are run: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Update CORS settings in production
- Set proper SECRET_KEY in production
- Configure proper database (PostgreSQL recommended)

---

## Version 1.0.0 - Initial Release

### Features
- Basic user authentication
- Patient, Doctor, Pharmacy, Lab roles
- Simple appointment booking
- Medicine inventory management
- Admin panel

---

## Upgrading from 1.0.0 to 2.0.0

### Breaking Changes
⚠️ **Database Schema**: New migrations required
⚠️ **Appointment Model**: Fields changed (datetime → date + time)
⚠️ **Status Enum**: Values changed (APPROVED → confirmed, etc.)

### Migration Steps
1. Backup your database
2. Pull latest code
3. Install new dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Update API clients to use new endpoint URLs
6. Test with new token refresh flow

### New Environment Variables
None required, but recommended:
- `JWT_ACCESS_TOKEN_LIFETIME`: Default 60 minutes
- `JWT_REFRESH_TOKEN_LIFETIME`: Default 7 days

---

## Future Roadmap

### Version 2.1.0 (Planned)
- [ ] Appointment reminders (email/SMS)
- [ ] Doctor reviews and ratings
- [ ] Payment integration
- [ ] Medical records upload
- [ ] Video consultation support

### Version 2.2.0 (Planned)
- [ ] Multi-language support
- [ ] Push notifications
- [ ] Advanced search with filters
- [ ] Analytics dashboard
- [ ] Export reports

---

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## Support
For issues, questions, or feature requests, please open a GitHub issue.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
