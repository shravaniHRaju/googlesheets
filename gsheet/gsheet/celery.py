from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gsheet.settings')

# Create a Celery instance
app = Celery('gsheet')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover task modules in Django applications
app.autodiscover_tasks()

# Define a task for debugging purposes
@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
