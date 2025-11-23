# 🏥 Medical Platform API Project

This project is a complete Back-End and API for a comprehensive medical platform built with Django and Django REST Framework. The project connects patients, doctors, pharmacies, and laboratories.

---

## ✨ Key Features

* **Advanced Role System:** 4 primary user types (Patient, Doctor, Lab, Pharmacy) in addition to an Admin.
* **Approval System:** Doctors, pharmacies, and labs cannot log in or appear in search results until they are approved by an admin (`is_approved=True`) via the Django admin panel.
* **JWT Authentication:** Secure login system using JSON Web Tokens (Simple JWT).
* **Integrated Appointment System:**
    * Patients can book appointments with doctors or labs.
    * Doctors/Labs can view their pending appointments and approve or reject them.
* **Medical History Access:** The patient's medical history is automatically visible to the doctor when viewing appointment details.
* **Profile Management:** Every user can edit their own profile data (`api/auth/me/`).
* **Pharmacy Inventory Management:**
    * Pharmacies can add, edit, and delete their own medicine stock.
    * Patients can view a list of pharmacies and their available (`in_stock=True`) medications.
* **Powerful Admin Panel:** For managing users, approvals, appointments, and medicines.

---

## 🛠️ Technologies Used

* Python 3
* Django
* Django REST Framework (DRF)
* Simple JWT (For Token Authentication)

---

## 🚀 Installation and Setup

1.  **Clone the project:**
    ```bash
    git clone (your-repo-link)
    cd MedicalPlatform
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # (Windows)
    python -m venv venv
    venv\Scripts\activate
    
    # (Mac/Linux)
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations (Create the database):**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin account):**
    ```bash
    python manage.py createsuperuser
    ```
    (Enter a username, email, and password)

6.  **Run the server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the Admin Panel:**
    Navigate to `http://127.0.0.1:8000/admin/` and log in."# backend-pharmacy-project" 
