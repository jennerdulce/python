<!-- Django Notes -->

## App
- Small pieces of project that mek up the the entire website
- Can have mutliple AP{s
- How you structure them is completely up to you
- Contains the following:
    - Models
    - Views
    - URLs
    - Templates
- APPs sit in main project folder and add them application settings file

## Views
- Functions that render views when users visit your website
- Flow:
    - User hits an endpoint
    - Endpoint is associated with a function
    - Function renders a webpage / html document
    - Beginner: Use function based views

## URl routing
- Creating url patterns

```python
urlpatterns =[
    path('profile/', views.profileView)
]
```

## Models
- How we create our database

## Django ORM
- Has built in ORM

## Admin Panel


## CRUD


## Static files
- Add in visual layer
- Styles
- JS
- Images

## Authentication
- Built in Method for authentication
- Registration
- Passwordreset
- Logout

## Django Commands
- django-admin startproject <project-name>
    - Boiler plate for django project
- python manage.py startapp <app-name>
    - Boiler plate for app
- python manage.py makemigrations
    - Preps 
- python manage.py migrate
- python manage.py createsuperuser
    - Creates user with admin level permission

## Production Database
- PostgresQL
- Settings file

## DJANGO REST frameworks

## Deployment
- 