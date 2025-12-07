# 🏥 Vezeeta-Style Medical Platform API

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14-red.svg)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive backend API for a medical platform similar to Vezeeta, built with Django and Django REST Framework. This system connects patients, doctors, pharmacies, laboratories, and radiology centers with complete CRUD operations and role-based access control.

---

## 🌟 Highlights

✨ **40+ API Endpoints** | 🔐 **JWT Authentication** | 👥 **6 User Roles** | 📅 **Smart Scheduling** | 🏥 **Complete CRUD Operations**

---

## ✨ Key Features

### 🔐 Authentication & Security
* **JWT Authentication** with access and refresh tokens
* **Secure Logout** with token blacklisting
* **Role-Based Access Control** (RBAC)
* **Admin Approval System** for medical providers
* **Password Encryption** with Django's built-in hashing

### 👥 User Roles
* **Patient** - Book appointments, manage profile
* **Doctor** - Manage schedule, view appointments  
* **Pharmacy** - Manage inventory, set working hours
* **Laboratory** - Manage tests, set schedules
* **Radiology** - Manage imaging services
* **Admin** - Complete platform management

### 🏥 Core Functionality
* **Appointment Booking** with date/time separation
* **Doctor Availability** management system
* **Working Hours** for all facilities
* **Medical History** tracking
* **Pharmacy Inventory** management
* **Reservation Cancellation** by patients
* **Advanced Filtering** and pagination

### 👨‍💼 Admin Capabilities
* Create and manage all user types
* Full CRUD operations for doctors
* View and filter all reservations
* Approve/reject medical providers
* Manage doctor availabilities
* System-wide oversight

---

## 🛠️ Technologies Used

* **Python 3.10+**
* **Django 4.2** - Web framework
* **Django REST Framework 3.14** - API toolkit
* **Simple JWT 5.3** - Token authentication
* **SQLite** - Development database (PostgreSQL recommended for production)
* **django-cors-headers** - CORS handling

---

## 📁 Project Structure

```
webapp/
├── accounts/           # User management & authentication
│   ├── models.py      # User, Profiles, WorkingHours, Availability
│   ├── serializers.py # User & Profile serializers
│   └── views.py       # Auth endpoints
├── api/               # Main API logic
│   ├── admin_views.py # Admin-only endpoints
│   ├── views.py       # Public & role-specific endpoints
│   ├── permissions.py # Custom permissions
│   └── urls.py        # URL routing
├── appointments/      # Reservation system
│   ├── models.py      # Appointment model
│   └── serializers.py # Reservation serializers
├── pharmacy/          # Medicine inventory
│   ├── models.py      # Medicine model
│   └── views.py       # Pharmacy endpoints
├── medical_project/   # Project settings
└── manage.py          # Django management script
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Farag-Sherif/backend-pharmacy-project.git
cd backend-pharmacy-project
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
# Follow the prompts to create admin user
```

### 6. Start Development Server
```bash
python manage.py runserver
```

Server will be running at: **http://127.0.0.1:8000/**

### 7. Access Admin Panel
Navigate to: **http://127.0.0.1:8000/admin/**

---

## 📚 Documentation

### Complete Guides
* **[API_SUMMARY.md](API_SUMMARY.md)** - Complete API documentation with all endpoints
* **[TESTING_GUIDE.md](TESTING_GUIDE.md)** - Testing guide with cURL examples
* **[CHANGELOG.md](CHANGELOG.md)** - Version history and changes
* **[APIDocs.md](APIDocs.md)** - Legacy API documentation

### Quick Links
* **API Base URL:** `http://127.0.0.1:8000/api/`
* **Admin Panel:** `http://127.0.0.1:8000/admin/`

---

## 🔑 API Endpoints Overview

### Authentication (`/api/auth/`)
```
POST   /patient/signup/     - Patient registration
POST   /login/              - Login (all roles)
POST   /refresh/            - Refresh access token
POST   /logout/             - Logout & blacklist token
GET    /me/                 - Get current user profile
PATCH  /me/                 - Update profile
```

### Admin (`/api/admin/`)
```
POST   /create-admin/                    - Create admin user
GET    /doctors/                         - List all doctors
POST   /doctors/                         - Create doctor
GET    /doctors/{id}/                    - Get doctor details
PUT    /doctors/{id}/                    - Update doctor
DELETE /doctors/{id}/                    - Delete doctor
POST   /doctors/{id}/availabilities/    - Set doctor schedule
POST   /pharmacies/                      - Create pharmacy
POST   /laboratories/                    - Create laboratory
POST   /radiologies/                     - Create radiology center
GET    /reservations/                    - View all reservations
```

### Public (`/api/`)
```
GET    /doctors/              - Browse doctors
GET    /pharmacies/           - Browse pharmacies
GET    /laboratories/         - Browse laboratories
GET    /radiologies/          - Browse radiology centers
```

### Patient (`/api/patient/`)
```
GET    /reservations/             - List my reservations
POST   /reservations/             - Book appointment
PUT    /reservations/{id}/cancel/ - Cancel reservation
```

### Doctor (`/api/doctor/`)
```
GET    /profile/              - Get my profile
GET    /reservations/         - View my appointments
```

### Working Hours
```
GET    /{type}/{id}/working-hours/    - Get facility hours
PUT    /{type}/{id}/working-hours/    - Set facility hours
```

---

## 🧪 Testing

### Using cURL
```bash
# Login
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Create Doctor (Admin)
curl -X POST http://127.0.0.1:8000/api/admin/doctors/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Ahmed",
    "last_name": "Hassan",
    "email": "doctor@example.com",
    "password": "doctor123",
    "specialization_name": "Cardiology",
    "experience": 5,
    "fee": 200.00
  }'
```

See **[TESTING_GUIDE.md](TESTING_GUIDE.md)** for complete testing examples.

---

## 🔒 Security Considerations

* **Token Expiry:** Access tokens expire after 1 hour
* **Refresh Tokens:** Valid for 7 days
* **Password Hashing:** Using Django's PBKDF2 algorithm
* **CORS:** Configure allowed origins in production
* **Admin Approval:** Providers must be approved before login
* **Role Permissions:** Strict role-based access control

---

## 📊 Database Models

### Core Models
* `User` - Custom user with role field
* `PatientProfile` - Patient-specific data
* `DoctorProfile` - Doctor credentials & specialization
* `PharmacyProfile` - Pharmacy details
* `LaboratoryProfile` - Lab information
* `RadiologyProfile` - Radiology center data

### Supporting Models
* `Specialization` - Medical specializations
* `WorkingHours` - Facility schedules
* `DoctorAvailability` - Doctor time slots
* `Appointment` - Patient reservations
* `Medicine` - Pharmacy inventory
* `BlacklistedToken` - Logout token management

---

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure production database (PostgreSQL)
- [ ] Set secure `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up HTTPS/SSL
- [ ] Configure static files serving
- [ ] Set up media file storage
- [ ] Configure CORS for frontend domain
- [ ] Set up logging
- [ ] Configure email backend
- [ ] Run security checks: `python manage.py check --deploy`

### Recommended Production Stack
* **Web Server:** Nginx or Apache
* **WSGI Server:** Gunicorn or uWSGI
* **Database:** PostgreSQL
* **Caching:** Redis
* **Task Queue:** Celery (optional)

---

## 📈 Performance Tips

* Use `select_related()` for foreign keys
* Use `prefetch_related()` for many-to-many
* Implement pagination for large datasets
* Use database indexes on frequently queried fields
* Enable query caching with Redis
* Use Django Debug Toolbar in development

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Farag Sherif**
- GitHub: [@Farag-Sherif](https://github.com/Farag-Sherif)

---

## 🙏 Acknowledgments

* Django & DRF communities
* Simple JWT library
* All contributors and testers

---

## 📞 Support

For issues, questions, or feature requests:
* Open a [GitHub Issue](https://github.com/Farag-Sherif/backend-pharmacy-project/issues)
* Check existing documentation
* Review the testing guide

---

## 🗺️ Roadmap

### Version 2.1.0
- [ ] Email/SMS notifications
- [ ] Doctor reviews & ratings
- [ ] Payment integration
- [ ] Medical records upload

### Version 2.2.0
- [ ] Multi-language support
- [ ] Push notifications
- [ ] Advanced analytics
- [ ] Video consultations

---

**Built with ❤️ using Django & Django REST Framework** 
