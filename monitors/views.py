from django.shortcuts import render
#moniter
from rest_framework import viewsets,views
from django.db import transaction
from django.shortcuts import render
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework import viewsets
from rest_framework.exceptions import APIException

from .models import Monitor, MonitorRequest,DeleteUrls
from .serializers import MonitorRequestSerializer, MonitorSerializer,DeleteUrlSerializer
import json
from rest_framework.response import Response


# Create your views here.
 #class UrlList(generics.ListCreateAPIView):
#     #list all teachers
#     queryset=UrlModel.objects.all()
#     serializer_class=UrlSerializer

# # CRONJOBS = [
# #     ('* * 2 * *', 'cron.my_cron_job')
# # ]
# from datetime import datetime
# import urllib.request

# # while True:
# #     a = datetime.now().second
# #     if (a % 15) == 0:  # every 15 seconds
        

# #         print(urllib.request.urlopen("https://www.stackoverflow.com").getcode())  # ---- To do something every 15 seconds ---- #
# #         while True:  # discard any milliseconds or duplicated 15 seconds
# #             a = datetime.now().second
# #             if (a % 15) is not 0:
# #                 break
# from django.shortcuts import HttpResponse
# from .task import test_func
# def test(request):
#     url='facebook.com'
#     test_func.delay()
#     return HttpResponse('Done')

class MonitorViewSet(viewsets.ModelViewSet):

    serializer_class = MonitorSerializer
    queryset = Monitor.objects.all()

    def perform_create(self, serializer):
        try:
            

                instance = serializer.save()
                schedule, created = IntervalSchedule.objects.get_or_create(
                    every=instance.interval,
                    period=IntervalSchedule.SECONDS,
                )

                task = PeriodicTask.objects.create(
                    interval=schedule,
                    name=f"Monitor: {instance.endpoint}",
                    task="monitors.task.task_monitor",
                    kwargs=json.dumps(
                        {
                            "monitor_id": instance.id,
                        }
                    ),
                )
                instance.task = task
                instance.save()

        except Exception as e:
            raise APIException(str(e))

    def perform_destroy(self, instance):
        print(instance.endpoint)
        DeleteUrls.objects.create(
            url=instance.endpoint
        )
        if instance.task is not None:

            instance.task.delete()
        return super().perform_destroy(instance)


class MonitorRequestViewSet(views.APIView):

     def get(self,request,id):
        print("//////")
        # teacher = Teacher.objects.filter(id=id)

        # print(teacher)
        requests = MonitorRequest.objects.filter(monitor=id)
        
        
        serializer = MonitorRequestSerializer(requests,many=True)
        
        return Response (serializer.data)

class DeleteUrl(views.APIView):
    def get(self,request):
        print("//////")
        # teacher = Teacher.objects.filter(id=id)

        # print(teacher)
        urls = DeleteUrls.objects.all()
        
        
        serializer = DeleteUrlSerializer(urls,many=True)
        
        return Response (serializer.data)