from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserAuthSerializer  # Replace with your actual serializer import
import random

class AuthenticateUser(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password1 = serializer.validated_data.get('password1')
            password2 = serializer.validated_data.get('password2')
            auth_token = str(random.randint(100001, 999999))

            if password1 == password2:
                authentication_email = EmailMessage(
                    'Authentication Token',
                    f'Here is your authentication token: {auth_token}',
                    'settings.EMAIL_HOST_USER',
                    [email]
                )
                authentication_email.send()

                return Response(auth_token, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'errors': [{'field': 'password', 'messages': ['Passwords do not match']}]},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            formatted_errors = []
            for field, messages in serializer.errors.items():
                formatted_errors.append({
                    'field': field,
                    'messages': messages,
                    'additional_info': f'Invalid {field} field',
                })
            return Response({'errors': formatted_errors}, status=status.HTTP_400_BAD_REQUEST)
