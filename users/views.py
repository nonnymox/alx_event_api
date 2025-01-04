from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import User
import logging

# Create a logger for logging exceptions or any errors
logger = logging.getLogger(__name__)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            # Authenticate user using the email and password
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                # If user is authenticated, log them in
                login(request, user)
                return Response({
                    'message': 'Login successful'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as e:
            # Log the exception for debugging purposes
            logger.error(f"Error during login: {str(e)}")
            return Response({'error': 'An error occurred during login.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
