# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1709303/data/www/hochunaves.ru/hochu')
sys.path.insert(1, '/var/www/u1709303/data/env/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hochu.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()