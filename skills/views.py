from django.views import View
from django.http import JsonResponse

from .models import Skill


class SkillList(View):
    def get(self, request):
        skills = Skill.objects.all()
        data = [skill.to_json() for skill in skills]
        return JsonResponse(data, safe=False)
