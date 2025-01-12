# Event Management API with JWT Authentication

This API allows users to manage events, including creating, retrieving, updating, and deleting events. Authentication is implemented using JSON Web Tokens (JWT) to ensure secure access.

---

## Features

1. **User Authentication**
   - User registration
   - User login (JWT authentication)
   - User logout
2. **Event Management**
   - Create, list, update, and delete events.
   - Automatically associate events with the authenticated user.
3. **Secure Endpoints**
   - JWT authentication ensures that only authorized users can access protected endpoints.
4. **Event Registration**
   - Register for event when the maximum capacity hasn't been reached.
   - View the capacity and the number of attendees..
   - View the waitlist (Only for authenticated users) 

---

## Technologies Used

- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For building RESTful APIs.
- **JWT (via DRF SimpleJWT)**: For authentication.

---

## Endpoints

### User Authentication

#### 1. **Register a New User**

- **Endpoint**: `/api/register/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
      "username": "example",
      "password": "password123",
      "email": "example@example.com"
  }
  ```
- **Response**:
  ```json
  {
      "id": 1,
      "username": "example",
      "email": "example@example.com"
  }
  ```

#### 2. **Login**

- **Endpoint**: `/api/login/`
- **Method**: `POST`
- **Payload**:
  ```json
  {
      "username": "example",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
  }
  ```

#### 3. **Logout**

- **Endpoint**: `/api/logout/`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
      "detail": "Successfully logged out"
  }
  ```

---

### Event Management

#### 1. **List All Events**

- **Endpoint**: `/api/events/`
- **Method**: `GET`
- **Response**:
  ```json
  [
      {
          "id": 1,
          "title": "Event 1",
          "description": "Description for Event 1",
          "date_time": "2025-02-15T10:00:00Z",
          "location": "New York",
          "status": "active",
          "capacity": 100,
          "created_at": "2025-01-09T14:21:56.113805Z",
          "organizer": 1
      }
  ]
  ```

#### 2. **Create an Event**

- **Endpoint**: `/api/events/`
- **Method**: `POST`
- **Headers**: `Authorization: Bearer <access_token>`
- **Payload**:
  ```json
  {
      "title": "New Event",
      "description": "This is a new event",
      "date_time": "2025-02-15T10:00:00Z",
      "location": "New York",
      "status": "active",
      "capacity": 100
  }
  ```
- **Response**:
  ```json
  {
      "id": 2,
      "title": "New Event",
      "description": "This is a new event",
      "date_time": "2025-02-15T10:00:00Z",
      "location": "New York",
      "status": "active",
      "capacity": 100,
      "created_at": "2025-01-09T14:21:56.113805Z",
      "organizer": "user1",
  }
  ```

#### 3. **Update an Event**

- **Endpoint**: `/api/events/<id>/`
- **Method**: `PUT`
- **Headers**: `Authorization: Bearer <access_token>`
- **Payload**:
  ```json
  {
      "title": "Updated Event",
      "description": "Updated description",
      "date_time": "2025-02-16T11:00:00Z",
      "location": "Los Angeles",
      "status": "active",
      "capacity": 150
  }
  ```
- **Response**:
  ```json
  {
      "id": 2,
      "title": "Updated Event",
      "description": "Updated description",
      "date_time": "2025-02-16T11:00:00Z",
      "location": "Los Angeles",
      "status": "active",
      "capacity": 150,
      "created_at": "2025-01-09T14:21:56.113805Z",
      "organizer": "user1"
  }
  ```

#### 4. **Delete an Event**

- **Endpoint**: `/api/events/<id>/`
- **Method**: `DELETE`
- **Headers**: `Authorization: Bearer <access_token>`
- **Response**:
  ```json
  {
      "detail": "Event deleted successfully"
  }
  ```
### Event Registration and Capacity

#### 1. **Register for Event**

- **Endpoint**: `/api/events/<id>/register`
- **Method**: `POST`
- **Headers**: `None Needed`
- **Payload**:
  ```json
  {
      "name": "NEW USER",
      "email": "newuser@mail.com"
  }
  ```
- **Response**:
  ```json
  {
      "Registered for event successfully"
  }
  ```

  #### 2. **View Capacity**

- **Endpoint**: `/api/events/<id>/capacity`
- **Method**: `GET`
- **Headers**: `None Needed`
- **Payload**:
- **Response**:
  ```json
  {
    "capacity": 100,
    "attendees_count": 2,
    "available_slots": 98
  }

  ```
 #### 3. **View Waitlist**

- **Endpoint**: `/api/events/<id>/waitlist`
- **Method**: `GET`
- **Headers**: `Authorization: Bearer <access_token>`
- **Payload**:
- **Response**:
  ```json
  {
    "waitlist": []
  }

  ```



---

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set up MySQL server and database in settings.py

4. Run migrations and start the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Access the API at:

   - `http://127.0.0.1:8000/`

---

## Authentication Workflow

1. Register a user using `/api/register/`.
2. Login to get the `access` and `refresh` tokens via `/api/login/`.
3. Include the `access` token in the `Authorization` header for all protected endpoints:
   ```
   Authorization: Bearer <access_token>
   ```
4. Use `/api/logout/` to invalidate the tokens when done.

---

## Notes
- Test endpoints using tools like Postman or cURL to validate functionality.

---

## License

This project is licensed under the MIT License
