# Django REST API Project

## Overview
This project is a RESTful API built using Django and Django REST framework. The API provides endpoints to manage resources efficiently and can be extended as per the application's requirements.

## Features
- Live Version of the API
- CRUD operations on various resources
- validation, filtering and sorting of results
- Detailed API documentation

## Technologies Used
- **Django**: High-level Python web framework
- **Django REST framework**: Powerful and flexible toolkit for building Web APIs
- **django-environ**: Environment variables for Django settings
- **dj-database-url**: Utilizes the `DATABASE_URL` environment variable to configure the database
- **gunicorn**: Python WSGI HTTP Server for UNIX
- **psycopg2-binary**: PostgreSQL database adapter for Python

## Prerequisites
- Python 3.x
- PostgreSQL
- pip (Python package installer)

## Setup

## Clone the Repository

- **Step 1**: git clone https://github.com/toriqulmahal6359/restPythonAPI.git
- **Step 2**: cd https://github.com/toriqulmahal6359/restPythonAPI.git
- **Step 3**: Open Terminal or CMD and run command 'pip install -r requirements.txt'
- **Step 4**: Run 'python manage.py runserver' command
- **Step 5**: It will direct to your default web-browser according to your setting
- **Step 6**: Most important!!! Create you .env file inside at the root project to run error-free server,
              To ensure the .env is correctly running, Use 'print' keyword to check that in terminal

## Links for the API

The API allows for managing orders, products, and order items and guide through you further process stepwise

List Products: GET https://mahal-django-rest-api.onrender.com/api/products/

Create Product: POST https://mahal-django-rest-api.onrender.com/api/products/

Retrieve Product: GET https://mahal-django-rest-api.onrender.com/api/products/{id}/

Update Product: PUT https://mahal-django-rest-api.onrender.com/api/products/{id}/

Partial Update Product: PATCH https://mahal-django-rest-api.onrender.com/api/products/{id}/

Delete Product: DELETE https://mahal-django-rest-api.onrender.com/api/products/{id}/

List Orders: GET https://mahal-django-rest-api.onrender.com/api/orders/

Create Order: POST https://mahal-django-rest-api.onrender.com/api/orders/

Retrieve Order: GET https://mahal-django-rest-api.onrender.com/api/orders/{id}/

Update Order: PUT https://mahal-django-rest-api.onrender.com/api/orders/{id}/

Partial Update Order: PATCH https://mahal-django-rest-api.onrender.com/api/orders/{id}/

Delete Order: DELETE https://mahal-django-rest-api.onrender.com/api/orders/{id}/
