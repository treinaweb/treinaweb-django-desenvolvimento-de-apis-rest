from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import SkillList


app_name = "skills"
urlpatterns = [
    path("", csrf_exempt(SkillList.as_view()), name="list"),
]
