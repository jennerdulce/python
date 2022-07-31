<!-- Django Notes -->

- Reference: [Django CRUD](https://www.youtube.com/watch?v=GieYIzvdt2U&ab_channel=TraversyMedia)

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

## Viewset
- Allows us to create FUll CRUD api without us having to set explicit methods

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

## Serializers 
- Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
- The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide a Serializer class which gives you a powerful, generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.
- Purpose: To take our model / queryset of leads and turn it into JSON

## Setup
- `pip3 install pipenv`
- `export PATH="$PATH:/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10"`
- `pipenv shell`
    - Creates `Pipfile`
    - All packages will go here
- `pipenv install django djangorestframework django-rest-knox`
    - Creates lock fill and adds dependencies to `Pipfile`
- `django-admin startproject nameofapp`
    - Create a folder with `manage.py` file
    - CLI for python
    - Create migrations
    - Run server
    - ETC
- `cd appname`
- `python manage.py startapp appname`
    - Creats app / folder called `appname`
    - Go to settings.py and add

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]


TO

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leads',
    'rest_framework'
]
```

## Setting up PostgresQL
- [Reference](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
- Create DB in postgreql
- In settings:

```python

REPLACE: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

NEW:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbtest', 
        'USER': 'postgres', 
        'PASSWORD': '1234',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```

- Create a model for the app
    - appname > models.py
- After model has been made
- `python manage.py makemigrations appname`
```
leads/migrations/0001_initial.py
    - Create model Lead
```
- `python manage.py migrate`
- Create `serializers.py` file within app
- appname >  `serializers.py`
- Within `serializers.py`

```python
from rest_framework import serializers
# Imported Lead class / model
from leads.models import Lead

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
```

- Create `api.py` file within app folder

```python
from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
```

## URLS

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('leads.urls')),
]

```

- Create new `urls.py` in app
- leads > urls.py

```python
from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
```

- Run server `python manage.py runserver`