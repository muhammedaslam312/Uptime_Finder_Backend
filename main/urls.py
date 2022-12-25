from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)



urlpatterns = [
    #login
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/',views.RegisterAccount.as_view()),
    # path('all_urls/',views.UrlList.as_view()),
    # path('post_url/',views.UrlList.as_view()),
    # path('celery/',views.test,name='test'),
    
    
]