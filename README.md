# Mini Hospital Management System

## Tech Stack
- Django (Backend)
- Django ORM
- PostgreSQL / SQLite
- Serverless Framework
- AWS Lambda (local simulation)

## Features
- Doctor signup and login
- Patient signup and login
- Doctor availability slots
- Patient appointment booking
- Slot blocking after booking
- Serverless email notification

## Architecture

Patient → Django Backend → Database  
                     ↓
             Serverless Email Service

## Running the Project

### Run Django

cd hms  
python manage.py runserver

### Run Serverless Email Service

cd email_service  
serverless offline

Then open:

http://127.0.0.1:8000
