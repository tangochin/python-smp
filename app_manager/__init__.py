import os
from django.apps import AppConfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_manager.settings')


class App(AppConfig):
    name = 'app_manager'
