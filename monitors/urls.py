from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import MonitorRequestViewSet, MonitorViewSet,DeleteUrl
from django.urls import path


router = DefaultRouter()
router.register(r"monitors", MonitorViewSet)
# router.register(r"requests", MonitorRequestViewSet)
monitors_urlpatterns = router.urls
urlpatterns = [
    #login
   
    path('requests/<int:id>/',MonitorRequestViewSet.as_view()),
    path('delete_url/',DeleteUrl.as_view()),
    # path('post_url/',views.UrlList.as_view()),
    # path('celery/',views.test,name='test'),
    
    
]