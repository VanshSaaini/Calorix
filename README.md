# 🥗 Calorix

**Calorix** is a modern Django-based web application designed to help users monitor their calorie intake, track nutritional information, and maintain a healthier lifestyle. The platform provides a user-friendly interface for managing health-related data while ensuring a secure and responsive user experience.

---

## 🚀 Features

* 🔐 Secure User Authentication (Signup/Login/Logout)
* 📊 Personalized Dashboard
* 🥗 Calorie & Nutrition Tracking
* 📱 Fully Responsive Design
* 🎨 Clean and Intuitive User Interface
* ⚡ Fast and Lightweight Django Backend

---

## 🛠️ Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Database

* SQLite (Development)

---

## 📸 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Login Page

![Login Page](screenshots/login.png)

### Dashboard

![Dashboard](screenshots/dashboard.png)

---

## 📂 Project Structure

```text
calorix/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── calorix/          # Project Configuration
├── home/             # Home & Authentication Module
├── dashboard/        # Dashboard Module
│
├── static/           # CSS, JavaScript, Images
├── templates/        # HTML Templates
└── screenshots/      # Project Screenshots
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/calorix.git
cd calorix
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/
```

---

## 🎯 Future Enhancements

* BMI Calculator
* BMR Calculator
* Personalized Meal Planning
* Weight & Progress Tracking
* Interactive Health Charts
* Nutrition Recommendations
* Food Database Integration
* Dark Mode Support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Vansh Saini**

* BCA Student at LPU
* Aspiring Full-Stack & Backend Developer
* Passionate about Python, Django, and Software Development

---

## 📄 License

This project is developed for educational, learning, and portfolio purposes.
