# Django Todo App

This is a simple Todo app built using Django. The app allows users to create, edit, complete and delete tasks. The app also allows the user to filter tasks by status. The app uses Django's built-in message framework to display success, error and info messages to the user. This version of the app does not include any session-based or authentication features, so all tasks will appear in one place and may be accessible to all users. 


## Screenshots

### Log In
![Log In](https://github.com/user-attachments/assets/046786c0-79b0-499f-9102-4e4d284935d0)

### Sign Up
![Sign Up](https://github.com/user-attachments/assets/c5fb6cb9-9467-4923-8d12-42bd8779f081)

### Index Page
![Index Page](https://github.com/user-attachments/assets/217738a2-ff1d-46f9-a8e0-878ae467057e)
### CRUD Operations
![image](https://github.com/user-attachments/assets/5e211bff-fdba-4f8a-97fd-e8df4f484fcd)
![image](https://github.com/user-attachments/assets/8a38b298-f8e1-4526-bd2e-2876aff84aa9)
![image](https://github.com/user-attachments/assets/9ebd826f-3960-4f51-bbab-98fe5da5d8fe)
## Mongo DB collections
![image](https://github.com/user-attachments/assets/c13f12aa-c98c-4c7d-9160-239bcab984f4)

## Features
- login
- sign up
- Create a new task
- Mark a task as completed or uncompleted
- Edit an existing task
- Delete a task
- Delete all tasks
- Filter tasks by status
- Display success, error and info messages to the user

## Requirements
- Python 3.x
- Django 3.x

## Setup
1. Clone the repository



2. Install the requirements

    `pip install -r requirements.txt`

3. Run migrations

    `python manage.py makemigrations`

    `python manage.py migrate`

4. Run the development server

    `python manage.py runserver`
    
5. Visit http://127.0.0.1:8000/ in your browser to access the app

## Code Structure
The code is structured as follows:
- The `models.py` file contains the Todo models
- The `forms.py` file contains the TodoForm and TodoFilterForm
- The `views.py` file contains the views for the app
- The `urls.py` file contains the URL patterns for the app
- The `templates` directory contains the HTML templates for the app
- The `static` directory contains the static files for the app (CSS, JS, etc)


## Support
If you need any help or have any questions, please feel free to contact me.

