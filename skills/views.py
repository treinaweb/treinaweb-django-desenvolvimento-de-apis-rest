import json
from django.views import View
from django.http import JsonResponse, HttpRequest

from .models import Skill


class SkillList(View):
    def get(self, request):
        skills = Skill.objects.all()
        data = [skill.to_json() for skill in skills]
        return JsonResponse(data, safe=False)

    def post(self, request: HttpRequest):
        body = json.loads(request.body)
        skill = Skill.objects.create(name=body["name"])
        return JsonResponse(skill.to_json())
