"""
ASGI config for project-sunshine project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.project-sunshine.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project-sunshine.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})
