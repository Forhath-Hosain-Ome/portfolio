from django.urls import path
from apps.blog.views import AurthorListApiView

urlpatterns = [
    path('aurthor/', AurthorListApiView.as_view()),
]
