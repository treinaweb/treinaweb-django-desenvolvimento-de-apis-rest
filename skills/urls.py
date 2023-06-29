from django.urls import path

from .views import SkillList, SkillDetail


app_name = "skills"
urlpatterns = [
    path("", SkillList.as_view(), name="list"),
    path("<int:pk>", SkillDetail.as_view(), name="detail"),
]
