from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtubeLatest.settings")

app = Celery("youtubeLatest")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# adding a import to the task
from .tasks import fetchVideosTask  # noqa: E402,F401
