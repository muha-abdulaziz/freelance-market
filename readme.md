# 🏆 Freelance Marketplace Platform

Welcome to the **Freelance Marketplace Platform**, a web application that connects freelancers with clients. Built using **Flask**, **MySQL**.

## 📌 Prerequisites

Before setting up the project, ensure you have:
- **Python 3.8+** installed
- **MySQL Server** running
- **pip** and **virtualenv** installed

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/freelance-marketplace.git
cd freelance-marketplace
```

### 2️⃣ Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```
If `requirements.txt` doesn’t exist, install manually:
```bash
pip install flask flask-mysql mysql-connector-python
```
Then, freeze dependencies:
```bash
pip freeze > requirements.txt
```

---
### 6️⃣ Run the Flask App
```bash
flask --app src run
```
Or set environment variables and run:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
For Windows:
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

---

## 🛠️ Common Issues

- **MySQL Connection Error?** Check if MySQL is running and credentials are correct.
- **Virtual Environment Not Activating?** Use full paths or check permissions.

---

## 🚀 Features
- User authentication (clients & freelancers)
- Posting jobs and bidding system
- Secure payment processing
- Real-time messaging
- Review and rating system

---
## Next steps
- Database migration
- Setup docker and docker compose
- Setup template engine
- Add guidelines

---

## 📜 License
This project is open-source. Feel free to modify and use it.