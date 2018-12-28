"""
WSGI config for presence project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get("DJANGO_ENV", "production") == "development":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presence.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presence.settings.production")

application = get_wsgi_application()
