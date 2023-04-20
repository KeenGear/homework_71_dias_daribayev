# Instagram Clone API #

This is a Django REST API project that serves as the backend for an Instagram clone application. The API provides endpoints for creating, retrieving, updating, and deleting posts, as well as for liking and unliking posts.

## Getting Started ##

To get started with this project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/KeenGear/homework_71_dias_daribayev.git
```
Install the project dependencies:
```
cd homework_71_dias_daribayev
pip install -r requirements.txt
```
Run database migrations:
```
python manage.py migrate
```
Create a superuser account:
```
python manage.py createsuperuser
```
Run fixtures:
```
python manage.py loaddata fixtures/auth.json
python manage.py loaddata fixtures/insta.json
python manage.py loaddata fixtures/users_app.json
```
Start the development server:
```
python manage.py runserver
```
You should now be able to access the API at http://localhost:8000/api/.

## API Endpoints ##

The following API endpoints are available:

### GET /api/posts/ ###
Returns a list of all posts.

### POST /api/posts/ ###
Creates a new post.

### GET /api/posts/<id>/ ###
Returns details for a specific post.

### PUT /api/posts/<id>/ ###
Updates a specific post.

### DELETE /api/posts/<id>/ ###
Deletes a specific post.

### POST /api/posts/<id>/like/ ###
Likes a specific post.

### DELETE /api/posts/<id>/like/ ###
Unlikes a specific post.

## Authentication ##

Most API endpoints require authentication. To authenticate, include a token in the Authorization header of your request:
```
Authorization: Token <your-token>
```
To obtain a token, send a POST request to the api-token-auth endpoint with your superuser account credentials:
```
{
    "username": "your-username",
    "password": "your-password"
}
```
The response will include your token:
```
{
    "token": "<your-token>"
}
```
