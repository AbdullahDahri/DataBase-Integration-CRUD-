# FastAPI MySQL Integration

A backend REST API project demonstrating the integration of **FastAPI** with a **MySQL** database using **SQLAlchemy ORM**. This project showcases how to build a scalable REST API with persistent data storage, dependency injection, request validation, and automatic API documentation.
The purpose of this project is to understand how FastAPI communicates with a relational database while following modern backend development practices.

# Project Overview

This project implements a RESTful API that performs CRUD (Create, Read, Update, Delete) operations on user data stored in a MySQL database.

The application uses:

- **FastAPI** for building high-performance REST APIs
- **SQLAlchemy** as the Object Relational Mapper (ORM)
- **MySQL** for persistent data storage
- **Pydantic** for request validation and response serialization
- **Dependency Injection** for database session management

# Features

- RESTful API development with FastAPI
- MySQL database integration
- SQLAlchemy ORM
- Pydantic request validation
- Pydantic response models
- CRUD operations
- Dependency Injection using `Depends()`
- Database session management
- Automatic Swagger API documentation
- Automatic ReDoc API documentation


#  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| MySQL | Relational Database |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |



# Project Structure

```text
FastAPI-MySQL-Integration/
│
├── database.py          # Database connection configuration
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic request & response schemas
├── main.py              # API endpoints
├── requirements.txt
├── README.md
└── .gitignore
```
# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-mysql-integration.git
```

## 2. Navigate to the Project Directory

```bash
cd fastapi-mysql-integration
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

# Configure MySQL

Create a MySQL database.

Update the database connection string inside `database.py` according to your local MySQL configuration.

Example:

```python
DATABASE_URL = "mysql+pymysql://root@localhost/fastapi_db"
```



# Run the Application

Start the FastAPI development server.

```bash
uvicorn main:app --reload
```

The application will run at:

```
http://127.0.0.1:8000
```

# API Documentation

After starting the server, FastAPI automatically generates API documentation.

### Swagger UI

http://127.0.0.1:8000/docs
```
### ReDoc

http://127.0.0.1:8000/redoc


# Implemented Operations

- Create User
- Retrieve All Users
- Retrieve User by ID
- Update User Information
- Delete User

# Concepts Demonstrated

This project demonstrates practical implementation of:

- FastAPI Routing
- REST API Development
- SQLAlchemy ORM
- MySQL Database Integration
- CRUD Operations
- Dependency Injection
- Database Sessions
- Pydantic Models
- Request Validation
- Response Models
- Automatic API Documentation



#  Request Flow

                Client
                   │
                   ▼
           FastAPI Endpoint
                   │
                   ▼
     Dependency Injection (Depends)
                   │
                   ▼
          Database Session
                   │
                   ▼
          SQLAlchemy ORM
                   │
                   ▼
            MySQL Database
                   │
                   ▼
        Pydantic Response Model
                   │
                   ▼
             JSON Response
```
# 🎯 Learning Objectives

The primary learning objectives of this project are:

- Understand FastAPI fundamentals
- Learn SQLAlchemy ORM
- Integrate MySQL with FastAPI
- Perform CRUD operations
- Manage database sessions efficiently
- Validate data using Pydantic
- Build RESTful APIs following backend development best practices

# Author

Abdullah Dahri


# 📄 License

This project is created for educational and learning purposes.
