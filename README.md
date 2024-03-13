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

### Installation

1. **Clone the repository**

git clone https://your-repository-url.git
cd your-project-directory

### Setting Up a Virtual Environment (Recommended)

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Using a virtual environment allows you to manage dependencies for different projects, avoiding conflicts between package versions. Setting up a virtual environment for this project is recommended to keep your dependencies isolated from your global Python installation.

1. **Create a Virtual Environment**

   Navigate to your project directory and run the following command to create a virtual environment named `venv`. You can name the environment anything you like.

   ```bash
   python -m venv venv
