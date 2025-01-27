# MyInfo Django API

## Project Overview

This project is a Django-based backend application that integrates with MyInfo v4 APIs provided by the Singapore Government Technology Agency (GovTech). The application allows users to authenticate via SingPass, authorize data sharing, and retrieve their personal information securely using OAuth 2.0 PKCE flow.

## Features

- SingPass authentication and authorization.
- Secure data retrieval from MyInfo resource server.
- OAuth 2.0 PKCE flow implementation.
- JSON Web Token (JWT) validation.
- Unit tests for API endpoints.

## Project Installation and Running

### Prerequisites

- Python 3.11
- PDM (Python Dependency Manager)

### Installation Steps

1. **Install PDM**

   If you haven't installed PDM, run:
   ```bash
   pip install pdm
   ```

2. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/myinfo-django-api.git
   cd myinfo-django-api
   ```

3. **Install dependencies**

   ```bash
   pdm install
   ```

4. **Run migrations**

   ```bash
   pdm run python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**

   ```bash
   pdm run python manage.py createsuperuser
   ```

6. **Run the Django development server**

   ```bash
   pdm run python manage.py runserver
   ```

7. **Run test cases**

   ```bash
   pdm run pytest
   ```

## API Usage

### 1. Authentication URL

**Endpoint:**
```http
GET /api/auth/login/
```

**Description:**
Returns the SingPass authorization URL for the user to log in.

**Response:**
```json
{
    "auth_url": "https://test.api.myinfo.gov.sg/..."
}
```

---

### 2. Authorization Callback

**Endpoint:**
```http
GET /api/auth/callback/?code=AUTH_CODE
```

**Description:**
Handles the authorization callback, exchanges the auth code for an access token, and retrieves user data from MyInfo.

**Response:**
```json
{
    "uinfin": "S1234567A",
    "name": "John Doe",
    "dob": "1990-01-01",
    "email": "johndoe@example.com"
}
```

---

### 3. Running API Tests

You can run tests using:
```bash
pdm run python manage.py test
```

Expected output should include successful test case execution without errors.

---

## Project Structure
```
myinfo_project/
│-- myinfo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│-- myinfo_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── tests.py
│-- templates/
│-- requirements.txt
│-- README.md
│-- .gitignore
```

---

## Environment Variables

Make sure to set the following environment variables in `.env`:
```plaintext
MYINFO_CLIENT_ID=your-client-id
MYINFO_CLIENT_SECRET=your-client-secret
MYINFO_REDIRECT_URI=http://localhost:3001/callback
MYINFO_API_URL=https://test.api.myinfo.gov.sg
```

