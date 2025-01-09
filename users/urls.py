from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    # User Registraion View
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    # JWT login view (obtain access token)
    path('login/', UserLoginView.as_view(), name='user-login'),
    # JWT refresh view (refresh access token using refresh token)
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    # Optional log out view as JWT handles log out
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
