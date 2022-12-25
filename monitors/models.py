from django.db import models

# Create your models here.
from django.db import models
from django_celery_beat.models import PeriodicTask


class Monitor(models.Model):

   
    endpoint = models.CharField(max_length=1024, blank=False)

   
    interval = models.IntegerField(blank=False)

    task = models.OneToOneField(PeriodicTask, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)


class MonitorRequest(models.Model):

   
    response_time = models.IntegerField(blank=False,null=True)
    response_status = models.IntegerField(blank=False)

    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True)

class DeleteUrls(models.Model):
    url=models.CharField(max_length=1024, blank=False)

