from django.urls import path

from .views import JobList


app_name = "jobs"
urlpatterns = [
    path("", JobList.as_view(), name="list"),
]
