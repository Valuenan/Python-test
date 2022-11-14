import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_test.settings')

app = Celery('drf_test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'statistics_everyday': {
        'task': 'manager.tasks.send_user_statistic',
        'schedule': crontab(hour=10)
    }
}
