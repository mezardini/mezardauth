from rest_framework import serializers
from django.core.validators import RegexValidator


class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[
        RegexValidator(
            regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
            message='Enter a valid email address.',
            code='invalid_email'
        )
    ])
    password1 = serializers.CharField(validators=[
        RegexValidator(
            regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=[\]{};\\|,.<>/?]).{8,}$',
            message='Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character.',
            code='invalid_password'
        )
    ])
    password2 = serializers.CharField(validators=[
        RegexValidator(
            regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=[\]{};\\|,.<>/?]).{8,}$',
            message='Password must contain at least 8 characters, including one uppercase letter, one lowercase letter, one digit, and one special character.',
            code='invalid_password'
        )
    ])