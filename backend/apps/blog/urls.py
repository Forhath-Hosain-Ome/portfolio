from django.urls import path
from apps.blog.views import AurthorApiView

urlpatterns = [
    path('aurthor/', AurthorApiView.as_view()),
]
