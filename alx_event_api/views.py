from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the Event Management API",
        "endpoints": [
            "/api/register/ - Create new user",
            "/api/users/ - Manage users",
            "/api/users/{id} - GET - Retrieves the user information, PUT - Updates the user profile REQUIRES AUTHENTICATION TOKEN",
            "/api/login/ - Login to user account(Get JWT access and refresh token for auth) ",
            "/api/events/ - List upcoming events",
            "/api/events/create/ - Create new event REQUIRES AUTHENTICATION TOKEN",
            "/api/events/<int>/ - GET - Retrieves detials of a specific event, PUT - Perform CRUD operations on the events REQUIRES AUTHENTICATION TOKEN",
            "api/events/<id>/capacity - GET - Retrieves the capacity of a specific event"
            "/api/token/ - Obtain token",
            "/api/token/refresh/ - Refresh token",
        ]
    })
