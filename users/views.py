from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

# User registration view
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Open to anyone

# User login view (using JWT token authentication)
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]  # Open to anyone

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if the user exists and the password is correct
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            # Generate JWT tokens (access and refresh tokens)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=400)

# User logout view (no need to manually delete tokens for JWT)
class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # For JWT, logout simply means the user should stop using their token.
        # The token is stateless, so there's no need to delete it from the server.
        return Response({'detail': 'Successfully logged out'}, status=200)
