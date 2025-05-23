"""
WSGI config for CRPR project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRPR.settings')

application = get_wsgi_application()

staticfiles_path = os.path.join(os.path.dirname(__file__), 'staticfiles')
os.makedirs(staticfiles_path, exist_ok=True)

application = WhiteNoise(application, root=settings.STATIC_ROOT, prefix='/static/')
application.add_files(settings.MEDIA_ROOT, prefix='/media/')

