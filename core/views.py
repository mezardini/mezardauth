from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import random
from django.core.mail import EmailMessage
from .serializers import UserAuthSerializer
from rest_framework import generics, status
# Create your views here.


class AuthenticateUser(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password1 = serializer.validated_data.get('password1')
            password2 = serializer.validated_data.get('password2')
            auth_token =  str(random.randint(100001,999999))

            if password1==password2:
                authentication_email = EmailMessage(
                        'Here', 'Here is the ' + auth_token + ' .', 'settings.EMAIL_HOST_USER', [email])
                authentication_email.send()

            return Response(auth_token, status=status.HTTP_200_OK)
        else:
            errors = serializer.errors
            formatted_errors = []
            for field, messages in errors.items():
                formatted_errors.append({
                    'field': field,
                    'messages': messages,
                    'additional_info': 'Inavlid '+ field + ' field',
                })
            return Response({'errors': formatted_errors}, status=status.HTTP_400_BAD_REQUEST)