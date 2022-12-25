# from celery import shared_task
# from datetime import datetime
# import urllib.request
# from .models import Hello
# from .models import UrlModel,UrlStatus
# import requests


# @shared_task(bind=True)
# def test_func(self):
#     urls=UrlModel.objects.values('url','id')
#     for i in urls:
#         id=i['id']
#         url_instance=UrlModel.objects.get(id=id)
#         print(i['url'])

#         print(id)
#         url=i['url']
#     # print(urls)
#         try:
#             s=requests.get(url).status_code
#             if s==200:
#                 status='Active'

#         except:
#             status='Down'
#         UrlStatus.objects.create(
#                     url=url_instance,
#                     added_time=datetime.now().time(),
#                     status=status


#                 )
  
#     return 'Done'

from datetime import datetime, timedelta
from decimal import Decimal

import requests
from celery import shared_task

from .models import Monitor, MonitorRequest


@shared_task(bind=True)
def task_monitor(self, monitor_id):

    try:

        monitor = Monitor.objects.get(pk=monitor_id)

        response = requests.get(monitor.endpoint, timeout=60)
        if response.status_code == 200:
            s='Active'
        else:
            s='Down'

        MonitorRequest.objects.create(
           
            response_status=response.status_code,
            monitor=monitor,
            created_at=datetime.now().time(),
            status=s,
        )
        

    except Exception as e:
        print(str(e), type(e))