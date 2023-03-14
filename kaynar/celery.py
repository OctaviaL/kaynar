import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kaynar.settings")

app = Celery("kaynar")
app.config_from_object("django.conf.settings", namespace="CELERY")


app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send_spam': {
#         'task': 'spam.tasks.send_spam',
#         'schedule': crontab(0, 0, day_of_month='2')
#     }
# }