import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quickfix.settings")  # Update with your actual settings
django.setup()

from django.contrib.auth.models import User  # Now models should work fine
