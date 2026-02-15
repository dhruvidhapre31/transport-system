# Transport Calculation System

A DRF application that generates transport quotes, create bookings for transport managed by admins.

# Pre-Requisites
- Python 3.11+
- PostgreSQL
- Celery
- Redis

# Installation
- Create a virtual environment
bash```
python -m venv .venv
```

- Activate environment
bash```
.venv\Scripts\activate
```

- Install requirements
bash```
pip install -r requirements.txt
```

# Setup Env
- Create a .env file with config same as mentioned in .env.temp

# Create Database
- Create database in PostgreSQL and run below command for data models creation:
bash```
python manage.py migrate
```

# Project Structure

root/
    transport/
        application/
        domain/
        interface/
        utils/
        asgi.py
        settings.py
        urls.py
        wsgi.py
    .env
    .env.sample
    .gitignore
    manage.py
    README.md

# API Endpoints

- api/auth/login [POST]
- api/auth/refresh [POST]
- api/quote [POST]
- api/bookings [GET, POST]
- api/bookings/{id} [POST]
