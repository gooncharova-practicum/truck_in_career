import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'truck_in_career.settings')

application = get_asgi_application()
