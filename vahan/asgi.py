# import os
# from django.core.asgi import get_asgi_application

# # Set the default settings module for the 'django' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vahan.settings')  # Change 'yourproject' to your project name

# # Get the ASGI application.
# application = get_asgi_application()
import os

# 👇 1. Update the below import lib
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from paymentApp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 👇 2. Update the application var
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
            URLRouter(
                websocket_urlpatterns
            )
        ),
})