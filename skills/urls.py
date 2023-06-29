from django.urls import path

from .views import SkillList


app_name = "skills"
urlpatterns = [
    path("", SkillList.as_view(), name="list"),
]
