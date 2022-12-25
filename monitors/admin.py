from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MonitorRequest)
admin.site.register(models.Monitor)
admin.site.register(models.DeleteUrls)
