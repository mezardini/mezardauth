# mezardauth

This is a lightweight email authentication API built with Django REST Framework (DRF). It provides a simple and secure way to handle user authentication using email verification.

## Features

- User registration with email verification
- Email verification endpoint
<!-- - Login endpoint with token-based authentication
- User profile management -->
<!-- - Password reset functionality -->

## Requirements

- Python 3.10.5
- Django 4.1.5
- Django REST Framework (DRF)
- SMTP server for sending email


## How it works

- Client sends user email and passwords(2 passwords)
- API generates a token, sends the token to the email and returns the token to the client