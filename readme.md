# Online Quiz System

This is a  online quiz system implemented using Django, Django REST framework, and JWT authentication. It allows users to take quizzes, view their scores, and provides an admin panel for managing quizzes and viewing reports.

## Prerequisites

- Python 3.x
- Django 4.0.2
- Django REST framework 3.13.1
- Django REST framework Simple JWT 5.1.0
- Django Ratelimit 3.0.0
- Git
- Knowledge of REST APIs, authentication (JWT/session-based login), and SQL

## Project Structure

```
quiz_system/
├── quiz_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __pycache__/
├── quiz/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── middleware.py
│   ├── tests.py
│   └── __pycache__/
├── manage.py
└── requirements.txt
```

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/syedsami1/Online-Quiz-System.git
   cd quiz_system
   ```

2. **Create a Virtual Environment**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### User Authentication

- **POST /login**: Authenticate user & return JWT token (Rate Limiting Applied)

### Quiz Management (Admin)

- **GET /quizzes**: Get quiz list
- **POST /quizzes**: Create a quiz
- **POST /quizzes/{id}/questions**: Map questions to quiz
- **GET /quizzes/{id}/participants**: Get all quiz participants list with status
- **GET /quizzes/{id}/response/{user-id}**: Get quiz response of a particular user (Rate Limiting Applied)

### Quiz Attempt (User)

- **GET /my-quizzes**: List quizzes with login user quiz status
- **POST /quizzes/{id}/start**: Start a quiz
- **POST /quizzes/{id}/submit**: Submit quiz responses
- **GET /quizzes/{id}/response**: Get quiz response of a login user (Rate Limiting Applied)

## Rate Limiting

Each user can make a maximum of 100 requests per second. If exceeded, the server will return `429 Too Many Requests` with a retry header.

## Middleware Configuration

In `quiz/middleware.py`:
```python
from django_ratelimit.middleware import RateLimitMiddleware
```

In `quiz_system/settings.py`:
```python
MIDDLEWARE = [
    ...,
    'django_ratelimit.middleware.RatelimitMiddleware',
]

RATELIMIT_VIEW = 'django_ratelimit.exceptions.Ratelimited'
```

## Running Tests

To run the test cases, use the following command:
```sh
python manage.py test
```

