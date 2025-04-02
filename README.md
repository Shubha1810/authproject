# Auth Project

This repository contains two Python projects:  
1. **Auth Service** - Handles authentication and user management.  
2. **User Project** - Implements user-related functionalities.

## Project Structure


UserProject
Introduction
UserProject is a simple user authentication system built using Flask. It allows users to sign up, log in, and verify their identity using JWT-based authentication. This project also includes API endpoints for retrieving user details and a protected "Hello" endpoint.
Features
* User Signup
* User Login
* JWT-based Authentication
* User Verification
* Protected Routes
* Database Integration with SQLite
Technologies Used
* Python (Flask Framework)
* Flask-JWT-Extended (For authentication)
* Flask-SQLAlchemy (For database operations)
* SQLite (Database)
* Docker (For containerization)
* GitHub (For code versioning)

How to Run the Project
Prerequisites
Before running the project, ensure you have the following installed on your system:
1. Python (Version 3.9 or later)
2. Pip (Python package manager)
3. Docker (Optional, if you want to run the project in a container)
Steps to Run the Project Locally
1. Clone the Repository
Open your terminal and run the following command to clone the project:
git clone https://github.com/your-username/UserProject.git
2. Navigate to the Project Directory
cd UserProject
3. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
4. Install Dependencies
pip install -r requirements.txt
5. Initialize the Database
python
>>> from database import db
>>> from main import app
>>> with app.app_context():
...     db.create_all()
...
>>> exit()
6. Run the Application
python main.py
The application will start on http://127.0.0.1:4000/

Running the Project Using Docker
If you prefer to run the project inside a Docker container, follow these steps:
1. Build the Docker Image
docker build -t userproject .
2. Run the Docker Container
docker run -p 4000:4000 userproject
Now, the application will be available at http://127.0.0.1:4000/

API Endpoints
1. User Signup
* Endpoint: /user/signup
* Method: POST
* Request Body:
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "password123",
  "dob": "2000-01-01",
  "phone": "1234567890"
}
* Response:
{
  "message": "User signed up successfully",
  "user": {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "dob": "2000-01-01",
    "phone": "1234567890",
    "user_id": 1
  },
  "token": "your_jwt_token"
}
2. User Login
* Endpoint: /user/login
* Method: POST
* Request Body:
{
  "email": "johndoe@example.com",
  "password": "password123"
}
* Response:
{
  "message": "Login successful",
  "token": "your_jwt_token",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
}
3. Get User Details (Protected Route)
* Endpoint: /user/<user_id>
* Method: GET
* Authorization: Bearer Token (JWT)
* Response:
{
  "user_id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com",
  "dob": "2000-01-01",
  "phone": "1234567890"
}
4. Verify User (Protected Route)
* Endpoint: /user/verify
* Method: GET
* Authorization: Bearer Token (JWT)
* Response:
{
  "message": "User is authorized",
  "user_id": 1
}
5. Hello (Protected Route)
* Endpoint: /hello
* Method: GET
* Authorization: Bearer Token (JWT)
* Response:
{
  "message": "Hello, World!",
  "user_id": 1
}

Notes
* Make sure to replace your_jwt_token with the actual JWT received after login/signup when accessing protected routes.
* SQLite is used as the default database. If required, you can modify main.py to use PostgreSQL or MySQL.
* For production use, it is recommended to change the JWT_SECRET_KEY in main.py.
