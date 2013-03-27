import os
import sys

path = '/home/japhy/internal/solarPocketFactory/Server/spf_sales'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'spf_sales.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()