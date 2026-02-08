from .views import ProjectListView
from django.urls import path

urlpatterns = [
    path('v1/blog/', ProjectListView.as_view()),
]
