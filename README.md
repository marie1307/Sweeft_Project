# Sweeft_Project
The Personalized Workout Plan System API is a RESTful service designed to help users create and manage customized workout plans, track fitness goals, and log exercise feedback. Built with Django and Django REST Framework, it supports user registration, login, and JWT-based authentication, providing a secure and scalable foundation for fitness tracking applications.

## Features

- **User Authentication**: Implements JWT for secure registration, login, and logout.
- **Custom Workout Plans**: Users can craft and modify their own workout plans.
- **Exercise Catalog**: Access to a wide range of exercises with descriptions and difficulty levels.
- **Feedback System**: Users can leave feedback on exercises for personal tracking and community advice.
- **Goal Tracking**: Set and monitor fitness goals over a specified timeframe.
- **RESTful API**: Easy to use REST API for integration with various frontend frameworks.

## Getting Started

Follow these instructions to get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your development machine:

- Python (3.8 or later recommended)
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Setup

To set up the project locally, follow these steps:
- Clone the repository: `git clone <repository-url>`
- Navigate to the project directory: `cd <project-folder>`
- Set up a virtual environment (recommended):
  python -m venv venv
  Windows: venv\Scripts\activate
  Unix/MacOS: source venv/bin/activate
- Install dependencies: pip install -r requirements.txt
- Apply migrations: python manage.py migrate
- Create a superuser: python manage.py createsuperuser
- Run the development server: python manage.py runserver
- Access the admin interface at http://localhost:8000/admin to manage exercises, workout plans, etc.

### API Endpoints

The API endpoints exposed by the application include:

- /api/exercises/: CRUD operations for managing exercises.
- /api/personal_plans/: CRUD operations for managing personal workout plans.
- /api/plan_exercises/: Manage exercises within personal plans.
- /api/goals/: CRUD operations for managing personal fitness goals.
- /api/registration/: User registration endpoint.
- /api/login/: User login endpoint.
- /api/logout/: User logout endpoint.

Refer to the API documentation or viewsets in views.py for more details on available endpoints and their usage.

### Permissions

Custom permission classes are defined in permissions.py to control access to different parts of the system. Permissions are based on user roles and ownership of resources such as personal workout plans and fitness goals.

### Filters

Custom filters are implemented to enable search and filtering of exercise objects based on various criteria such as difficulty level, equipment required, and target muscles.

### Authentication

JWT-based authentication is implemented using Django REST Framework's Simple JWT. Users can obtain a token by logging in and use it to authenticate subsequent requests to protected endpoints.

### Deployment

For deployment, make sure to configure the appropriate settings for your production environment, including database settings, security settings, and environment variables. Consider using a platform-as-a-service (PaaS) provider such as Heroku or AWS Elastic Beanstalk for easy deployment and scalability.

Feel free to explore and modify the script according to your needs. This project was created for Sweeft acceleration project (II stage) by Mariam Kalmakhelidze.
