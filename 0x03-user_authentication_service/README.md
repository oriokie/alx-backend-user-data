# User Authentication Service

## 📝 Description

This project implements a user authentication service using Python, Flask, and SQLAlchemy. It covers various aspects of user authentication, including user registration, login, session management, and password reset functionality.

## 🎯 Learning Objectives

By the end of this project, you should be able to explain:

- [x] How to declare API routes in a Flask app
- [x] How to get and set cookies
- [x] How to retrieve request form data
- [x] How to return various HTTP status codes
- [x] The implementation of authentication mechanisms

## 🛠 Requirements

- Python 3.7
- Flask
- SQLAlchemy 1.3.x
- bcrypt

## 🚀 Setup

1. Install bcrypt:

   ```bash
   pip3 install bcrypt
   ```

2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/alx-backend-user-data.git
   ```

3. Navigate to the project directory:
   ```bash
   cd alx-backend-user-data/0x03-user_authentication_service
   ```

## 📁 Project Structure

| File      | Description                               |
| --------- | ----------------------------------------- |
| `user.py` | Defines the User model                    |
| `db.py`   | Implements database operations            |
| `auth.py` | Handles authentication logic              |
| `app.py`  | Contains the Flask application and routes |

## ✨ Features

- User registration
- User login and logout
- Session management
- Password hashing
- Password reset functionality

## 🖥 Usage

Run the Flask application:

```bash
python3 app.py
```

The server will start on `http://0.0.0.0:5000/`.

## 🔗 API Endpoints

| Method | Endpoint          | Description              |
| ------ | ----------------- | ------------------------ |
| POST   | `/users`          | Register a new user      |
| POST   | `/sessions`       | Log in a user            |
| DELETE | `/sessions`       | Log out a user           |
| GET    | `/profile`        | Get user profile         |
| POST   | `/reset_password` | Request a password reset |
| PUT    | `/reset_password` | Update password          |

## 🧪 Testing

You can use `curl` commands to test the various endpoints. Here's an example:

```bash
curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'
```

More examples are provided in the project description.

## 👤 Author

Kenyansa Edwin Orioki

## 🙏 Acknowledgements

This project is part of the ALX Backend User Data curriculum.
