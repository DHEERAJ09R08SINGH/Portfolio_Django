# 🌐 Django Portfolio Website with REST API

A **Django-based personal portfolio website** featuring a contact form with **database integration** and **RESTful APIs** built using **Django REST Framework (DRF)**.
This project demonstrates backend development skills including API design, server-side validation, and authentication-ready endpoints.

---

## 🚀 Features

* Responsive personal portfolio website
* Contact form with data stored in database
* REST APIs for creating and retrieving contact messages
* Server-side validation for secure data handling
* Authentication-protected API endpoints
* Admin panel for managing contact messages
* Scalable project structure

---

## 🛠 Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Database:** SQLite (development)
* **Frontend:** HTML, CSS, Bootstrap
* **Tools:** Git, GitHub

---

## 📂 Project Structure

```
Portfolioproject/
│── Portfolioapp/
│   │── migrations/
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── serializers.py
│   │── views.py
│   │── urls.py
│── Portfolioproject/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── templates/
│── static/
│── db.sqlite3
│── manage.py
```

---

## 🔗 REST API Endpoints

### ➤ Create Contact Message

```
POST /api/contacts/
```

**Request Body (JSON):**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "content": "Hello, I would like to connect."
}
```

---

### ➤ Get All Contact Messages (Authenticated)

```
GET /api/contacts/
```

---

## 🔐 Authentication

* Uses **Session Authentication**
* Protected endpoints require user login
* Admin access enabled for managing messages

---

## ⚙️ Installation & Setup

1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
```

2️⃣ Navigate to the project directory

```bash
cd Portfolioproject
```

3️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

5️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6️⃣ Create superuser

```bash
python manage.py createsuperuser
```

7️⃣ Run the development server

```bash
python manage.py runserver
```

---



## 👨‍💻 Author

**Dheeraj R Singh**


🔗 GitHub: [https://github.com/DHEERAJ09R08SINGH](https://github.com/DHEERAJ09R08SINGH)


🔗 LinkedIn: [https://www.linkedin.com/in/dheeraj-r-singh/](https://www.linkedin.com/in/dheeraj-r-singh-9b4370250/)


---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates me to build more!

---


