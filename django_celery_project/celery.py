import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule ={
    "send_mail_on_every_friday_10PM_IST":{
        'task':'mail.tasks.dj_send_mail',
        'schedule':crontab(hour = 1, minute=25)
    }
}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')