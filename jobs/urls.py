from django.urls import path

from .views import JobList, JobDetail


app_name = "jobs"
urlpatterns = [
    path("", JobList.as_view(), name="list"),
    path("<int:pk>", JobDetail.as_view(), name="detail"),
]
