# 🏥 Medical Platform API Documentation (APIDocs.md)

This is the complete documentation for all API endpoints for the medical platform.

**Base URL:** `http://127.0.0.1:8000/`

---
---

## 🔒 Authentication & User Management

**Base URL for this section:** `api/auth/`

---

### 1. Register Patient
* **Endpoint:** `register/patient/`
* **Method:** `POST`
* **Permissions:** `AllowAny`
* **Description:** Registers a new patient account. The account is auto-approved (`is_approved=True`).

---

### 2. Register Doctor
* **Endpoint:** `register/doctor/`
* **Method:** `POST`
* **Permissions:** `AllowAny`
* **Description:** Registers a new doctor account. Requires admin approval (`is_approved=False`).

---

### 3. Register Pharmacy
* **Endpoint:** `register/pharmacy/`
* **Method:** `POST`
* **Permissions:** `AllowAny`
* **Description:** Registers a new pharmacy account. Requires admin approval (`is_approved=False`).

---

### 4. Register Lab
* **Endpoint:** `register/lab/`
* **Method:** `POST`
* **Permissions:** `AllowAny`
* **Description:** Registers a new laboratory account. Requires admin approval (`is_approved=False`).

---

### 5. Login
* **Endpoint:** `login/`
* **Method:** `POST`
* **Permissions:** `AllowAny`
* **Description:** Authenticates a user (with `username` and `password`). Returns `access` and `refresh` tokens. Fails if the account is not approved.

---

### 6. Refresh Token
* **Endpoint:** `token/refresh/`
* **Method:** `POST`
* **Permissions:** `AllowAny`
* **Description:** Renews an expired `access token` using a valid `refresh token`.

---

### 7. Get/Update User Profile
* **Endpoint:** `me/`
* **Method:** `GET`, `PATCH`, `PUT`
* **Permissions:** `IsAuthenticated` (Logged-in user only)
* **Description:**
    * `GET`: Fetches the profile data for the currently logged-in user.
    * `PATCH`/`PUT`: Updates the profile data (both base user and specific profile) for the logged-in user.

---
---

## 🩺 Doctors

**Base URL for this section:** `api/`

---

### 1. List Doctors (For Patient)
* **Endpoint:** `doctors/`
* **Method:** `GET`
* **Permissions:** `IsAuthenticated` (Logged-in user)
* **Description:** Displays a list of all **approved** doctors (`is_approved=True`).

---

### 2. View Doctor's Appointments (For Doctor)
* **Endpoint:** `doctors/my-appointments/`
* **Method:** `GET`
* **Permissions:** `IsDoctor` (Doctors only)
* **Description:** Lists all appointments for the logged-in doctor. The patient's medical history (`medical_history`) is included in the appointment details.

---
---

## 🔬 Laboratories

**Base URL for this section:** `api/`

---

### 1. List Labs (For Patient)
* **Endpoint:** `labs/`
* **Method:** `GET`
* **Permissions:** `IsAuthenticated` (Logged-in user)
* **Description:** Displays a list of all **approved** labs (`is_approved=True`).

---

### 2. View Lab Details (For Patient)
* **Endpoint:** `labs/<int:pk>/`
* **Method:** `GET`
* **Permissions:** `IsAuthenticated` (Logged-in user)
* **Description:** Shows the details for a specific lab (using its User ID as `pk`).

---

### 3. View Lab's Appointments (For Lab)
* **Endpoint:** `labs/my-appointments/`
* **Method:** `GET`
* **Permissions:** `IsLab` (Labs only)
* **Description:** Lists all appointments for the logged-in lab.

---
---

## 🏥 Pharmacies

**Base URL for this section:** `api/`

---

### 1. List Pharmacies (For Patient)
* **Endpoint:** `pharmacies/`
* **Method:** `GET`
* **Permissions:** `IsAuthenticated` (Logged-in user)
* **Description:** Displays a list of all **approved** pharmacies (`is_approved=True`).

---

### 2. View Pharmacy Details & Medicines (For Patient)
* **Endpoint:** `pharmacies/<int:pk>/`
* **Method:** `GET`
* **Permissions:** `IsAuthenticated` (Logged-in user)
* **Description:** Shows details for a specific pharmacy and a list of its available (`in_stock=True`) medicines.

---

### 3. Manage Pharmacy Inventory (For Pharmacy)
* **Endpoint:** `pharmacies/my-medicines/`
* **Method:** `GET`, `POST`
* **Permissions:** `IsPharmacy` (Pharmacies only)
* **Description:**
    * `GET`: Lists the medicines belonging to the logged-in pharmacy.
    * `POST`: Adds a new medicine to the pharmacy's inventory.

---

### 4. Manage Specific Medicine (For Pharmacy)
* **Endpoint:** `pharmacies/my-medicines/<int:pk>/`
* **Method:** `GET`, `PATCH`, `PUT`, `DELETE`
* **Permissions:** `IsPharmacy` (Pharmacies only)
* **Description:** Retrieve, update, or delete a specific medicine (using the Medicine's ID as `pk`) from the pharmacy's inventory.

---
---

## 📅 Appointments

**Base URL for this section:** `api/`

---

### 1. Book Appointment (For Patient)
* **Endpoint:** `appointments/book/`
* **Method:** `POST`
* **Permissions:** `IsPatient` (Patients only)
* **Description:** Creates a new appointment. Must send either a `doctor` ID or `laboratory` ID in the request body.

---

### 2. Manage Appointment (For Doctor/Lab)
* **Endpoint:** `appointments/<int:pk>/manage/`
* **Method:** `GET`, `PATCH`, `PUT`
* **Permissions:** `IsAppointmentOwner` (Owner of the appointment only)
* **Description:**
    * `GET`: View details for a specific appointment.
    * `PATCH`/`PUT`: Update the appointment's status (e.g., to `APPROVED` or `REJECTED`).