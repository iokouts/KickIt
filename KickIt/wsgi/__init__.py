"""
WSGI config for KickIt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KickIt.settings.base")

application = get_wsgi_application()
application = WhiteNoise(application)

# Add media files
if settings.MEDIA_ROOT and settings.MEDIA_URL:
    application.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
