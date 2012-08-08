import os
import logging
import datetime

from celery.schedules import crontab

from chronam.settings import *

APP_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

BROKER_BACKEND = "djkombu.transport.DatabaseTransport"

INSTALLED_APPS += ("djkombu", "djcelery" )

CELERY_IMPORTS = ("chronam.core.tasks",)
CELERYD_LOG_FILE = os.path.join(APP_DIR, "logs", "celery.log")
CELERYD_LOG_LEVEL = logging.INFO
CELERYD_CONCURRENCY = 2

CELERYBEAT_SCHEDULE = {
    "poll_cts": {
        "task": "chronam.core.tasks.poll_cts",
        "schedule": datetime.timedelta(seconds=30),
        "args": ()
    },
    # Executes every morning at 2:00 A.M
    "delete_django_cache": {
        "task": "chronam.core.tasks.delete_django_cache",
        "schedule": crontab(hour=2, minute=0),
    }
}

CELERYBEAT_LOG_FILE = os.path.join(APP_DIR, "logs", "celerybeat.log")
CELERYBEAT_LOG_LEVEL = logging.INFO
