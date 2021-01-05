# Flask server Boilerplate

## Features:

- Environtment: production/development
- Middleware JWT
- Task-Celery
- Model
- Api register/login
- Migrations

## Install dependencies

pip install -r requirements.txt

### Environtment example

cp app/config/.env.example app/config/.env

## Production

### Run Celery

FLASK_ENV=.env.production celery -A app.tasks.celery worker --loglevel=INFO

### Run main app

FLASK_ENV=.env.production python main.py

## Development

### Run Celery

FLASK_ENV=.env.development celery -A app.tasks.celery worker --loglevel=INFO

### Run main app

FLASK_ENV=.env.development python main.py

### Enable celery event

celery -A app.tasks.celery control enable_events

## Migrations

flask db init

flask db migrate

flask db upgrade

## API:

### Register

```
POST http://0.0.0.0:3000/api/v1/register
Body:
{
	"email": "lyntc.elec@gmail.com",
    "username": "Ly Nguyen",
    "first_name": "Ly",
    "last_name": "Nguyen",
	"password": "12345678",
    "confirm_password": "12345678"
}

Response:
{
    "msg": "success",
    "status": 0
}
```

### Login

```
POST http://0.0.0.0:3000/api/v1/login
Body:
{
	"email": "lyntc.elec@gmail.com",
    "username": "Ly Nguyen",
	"password": "12345678"
}

Response:
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDEzNTAyOTgsIm5iZiI6MTYwMTM1MDI5OCwianRpIjoiNjQwNTNlMzQtZTk0Ny00Nzk0LTliNWMtNzgyMjczM2ZjZjc5IiwiZXhwIjoxNjAxMzUxMTk4LCJpZGVudGl0eSI6Imx5bnRjLmVsZWNAZ21haWwuY29tIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mE-LuzIzeZtzNQQBCYCIX7-XZKVc5BbKl8gFDBklTeg",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDEzNTAyOTgsIm5iZiI6MTYwMTM1MDI5OCwianRpIjoiYzJiNmNlM2YtOTY5Ni00YjAxLWJjMTMtMWNhNjNjZmIwMTZmIiwiZXhwIjoxNjAzOTQyMjk4LCJpZGVudGl0eSI6Imx5bnRjLmVsZWNAZ21haWwuY29tIiwidHlwZSI6InJlZnJlc2gifQ.FwgpR9n8Enkf5kmcLBfQ56mxtOwAT7rbqr-7RoVLSv8",
    "msg": "success",
    "status": 0
}
```

### Logout

```
GET http://localhost:3000/api/v1/user/logout
Header:
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDEzNTAyOTgsIm5iZiI6MTYwMTM1MDI5OCwianRpIjoiNjQwNTNlMzQtZTk0Ny00Nzk0LTliNWMtNzgyMjczM2ZjZjc5IiwiZXhwIjoxNjAxMzUxMTk4LCJpZGVudGl0eSI6Imx5bnRjLmVsZWNAZ21haWwuY29tIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.mE-LuzIzeZtzNQQBCYCIX7-XZKVc5BbKl8gFDBklTeg

Response:
{
    "msg": "You have successfully been logged out.",
    "status": 0
}
```

## Reference:

https://www.digitalocean.com/community/tutorials/build-a-crud-web-app-with-python-and-flask-part-one
https://github.com/cyberj0g/flask-deploy.git
