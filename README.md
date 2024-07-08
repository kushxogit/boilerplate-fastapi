# Welcome to the Project Onboarding Document

**Welcome aboard!** Please follow these steps to set up your development environment.

Repository:

## Setup Instructions

1.  **Install Python 3.11.x**
    Make sure you have the latest version of Python installed on your machine.

2.  **Check if pip is installed**
    Confirm pip installation by running the following command in your terminal:
    ```shell
    pip --version

    ```
3.  **Install Required Packages**
    Install all the necessary packages using pip by executing:
    ```shell
    pip install -r requirements.txt
    Note: The requirements.txt file can be found in our project directory.

4.  **Run the Application**
    To start the application, use the following command:

        uvicorn main:app --reload

# Understand the Project Structure

Please familiarize yourself with the files listed below, in the order provided. Each file includes comments explaining its purpose and usage.

I have structured our project into two modules: src and test:

```
└── backend/
    ├── src/
    │   ├── config/
    │   ├── routes/
    │   ├── util/
    │   └── __init__.py
    ├── test/
    │   ├── routes/
    │   ├── test_util/
    │   ├── __init.py__
    │   ├── app_test.py
    │   └── conftest.py
    ├── main.py
    └── requirements.txt
```

# Test module: TBD(To be done)

# File Descriptions

## Backend Main Entry Point

- Path:`backend/main.py`
- File Name: `main.py`
- Description: Serves as the main entry point for the FastAPI application, setting up routes and middleware.

## Database Configuration

- Path: `backend/src/config/database.py`
- File Name:`database.py`
- Description: Configures the MongoDB database connection and initializes Beanie for ORM operations.

## Application Configuration

- Path: `backend/src/config/config.py`
- File Name: `config.py`
- Description: Contains essential configuration variables such as the application name, version, and frontend URL.

# Folder Structure & Descriptions for backend/src/routes/auth

## internal/

Description: Houses internal logic for authentication, such as user data fetching and JWT token handling.

## rest_api/

Description: Contains the API endpoints for authentication services like login and token verification.

## store/

Description: Includes the data models and schemas used for authentication, featuring MongoDB document models and Pydantic validation schemas.

# For Backend Development, We will be focusing on the folder `routes` below

```
└── backend/
    └── src/
        └── routes/
            ├── auth/
            │   ├── internal/
            │   │   ├── auth_reader.py
            │   │   └── auth_writer.py
            │   ├── rest_api/
            │   │   └── auth_controller.py
            │   ├── store/
            │   │   ├── auth_models.py
            │   │   └── auth_schemas.py
            │   ├── auth_main.py
            │   └── auth_service.py
            └── __init__.py
```

## Authentication Logic - Internal

- Path: `backend/src/routes/auth/internal/auth_reader.py`
- File Name: `auth_reader.py`
- Description: Provides functionality to fetch user data from the database.
- Generalized Responsibilities: Used for reading data from the database.

- Path: `backend/src/routes/auth/internal/auth_writer.py`
- File Name: `auth_writer.py`
- Description: Manages JWT token creation and decoding.
- Generalized Responsibilities: Responsible for writing data, specifically creating and managing tokens.

## Authentication Endpoints - REST API

- Path: `backend/src/routes/auth/rest_api/auth_controller.py`
- File Name: `auth_controller.py`
- Description: Hosts API endpoints for authentication, including login and token verification.
- Generalized Responsibilities: Serves as the interface for HTTP requests handling authentication processes.

## Authentication Data Models and Schemas

- Path: `backend/src/routes/auth/store/auth_models.py`
- File Name: `auth_models.py`
- Description: Defines MongoDB document models for user credentials.
- Generalized Responsibilities: Defines the structure of data for storage and retrieval.

- Path: `backend/src/routes/auth/store/auth_schemas.py`
- File Name: `auth_schemas.py`
- Description: Specifies Pydantic models for authentication-related schemas.
- Generalized Responsibilities: Used for data validation and serialization.

## Authentication Routing Setup

- Path: `backend/src/routes/auth/auth_main.py`
- File Name: `auth_main.py`
- Description: Sets up the API router for authentication-related endpoints.
- Generalized Responsibilities: Configures routing and endpoint registration for the application.

##Authentication Service Provider

- Path: `backend/src/routes/auth/auth_service.py`
- File Name: `auth_service.py`
- Description: Offers methods for user authentication and token verification.
- Generalized Responsibilities: Provides service logic centralizing business rules and operations.
