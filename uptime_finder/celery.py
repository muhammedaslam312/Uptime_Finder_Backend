from __future__ import absolute_import , unicode_literals
import os

# from celery import Celery
# from django.conf import settings
# from celery.schedules import crontab  



# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uptime_finder.settings')
# app = Celery('uptime_finder')
# app.conf.enable_utc = False



# app.config_from_object(settings, namespace='CELERY')

# CELERY BEAT SETTING
# CELERY BEAT SETTING
# app.conf.beat_schedule = {

#     'call_url' : {
#     'task' : 'main.task.test_func',
#     'schedule' : crontab(),
#    }
# }

# # @app.on_after_configure.connect
# # def setup_periodic_tasks(sender, **kwargs):
# #     # Calls test('hello') every 10 seconds.
# #     sender.add_periodic_task(10.0, debug_task.s(), name='add every 10')

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request{self.requsest!r}')
# app.autodiscover_tasks()

import os
import sys

from celery import Celery

CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CURRENT_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uptime_finder.settings")

app = Celery("uptime_finder")
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()