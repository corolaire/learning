import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#configure database

# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_database',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',  # o la dirección IP de tu servidor de base de datos
        'PORT': '3306',  # el puerto predeterminado de PostgreSQL
    }
}
