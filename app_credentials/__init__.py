import os
from django.apps import AppConfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_credentials.settings')


class App(AppConfig):
    name = 'app_credentials'
