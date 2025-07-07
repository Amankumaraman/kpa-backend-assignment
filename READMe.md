# 🚆 KPA Backend Assignment – API Implementation (Django + PostgreSQL)

This project implements three backend API endpoints based on the provided `KPA_form data.postman_collection.json`. The APIs handle form submissions and querying for wheel specifications and bogie checksheets in a railway system.

---

## 🧰 Tech Stack

- **Backend Framework:** Django 4 + Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Environment Config:** `.env` file for DB credentials
- **Tools:** Postman (for testing), DRF Serializers, JSON handling

---

## 📌 Implemented API Endpoints

| Method | Endpoint                                     | Description                            |
|--------|----------------------------------------------|----------------------------------------|
| POST   | `/api/forms/wheel-specifications`            | Submit Wheel Specification Form        |
| GET    | `/api/forms/wheel-specifications`            | Get Wheel Specifications with Filters  |
| POST   | `/api/forms/bogie-checksheet`                | Submit Bogie Checksheet Form           |

---

## 🚀 Setup Instructions

### 1. 📁 Clone the Repository or Unzip
```bash
git clone https://github.com/Amankumaraman/kpa-backend-assignment.git
cd kpa-backend-assignment
````

### 2. 🐍 Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

### 3. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 4. 🛠️ Configure PostgreSQL via `.env`

Create a `.env` file in the root directory:

```env
DB_NAME=kpa_assignment
DB_USER=postgres
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

### 5. ⚙️ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. ▶️ Run the Server

```bash
python manage.py runserver
```

---

## 🔍 API Testing (via Postman)

### 📤 Postman Collection:

Import the file: `aman_kpa_postman.json`

**Test Endpoints:**

* `POST /api/forms/wheel-specifications`
* `GET  /api/forms/wheel-specifications?formNumber=...&submittedBy=...`
* `POST /api/forms/bogie-checksheet`

Expected responses:

* Status: `201 Created` or `200 OK`
* JSON structure with `success`, `message`, `data` fields

---

## 📄 File Structure (Important Files)

```
kpa_backend_assignment/
├── forms_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── kpa_assignment/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── .env
├── requirements.txt
├── aman_kpa_postman.json
└── README.md
```

---

## 🎥 Video Demo

📽️ Video Link: `https://drive.google.com/file/d/aman_kpa_assignment_demo.mp4`

Demo includes:

* Server setup
* Testing APIs in Postman
* Code explanation

---

## ✅ Status

All APIs are implemented, tested, and aligned 100% with the provided Postman collection and assignment specs.

---

## 💡 Optional Enhancements (Implemented or Suggested)

* ✅ DRF input validation via serializers
* ✅ Environment-based DB config using `.env`
* 🔄 Swagger integration (optional – can be added with `drf-yasg`)

---

## 🙋‍♂️ Author

**Aman Kumar**
GitHub: [github.com/Amankumaraman](https://github.com/Amankumaraman)
Portfolio: [devaiak.vercel.app](https://devaiak.vercel.app)

```
