import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve().parent.parent
os.makedirs(os.path.join(BASE_DIR, "staticfiles"), exist_ok=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RINL.settings')

application = get_wsgi_application()
