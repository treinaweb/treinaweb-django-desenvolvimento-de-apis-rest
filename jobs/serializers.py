from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ("is_active",)
        extra_kwargs = {
            "title": {"min_length": 10},
            "salary": {"min_value": 1000},
            "description": {"min_length": 10, "max_length": 500},
            "company": {"min_length": 3},
            "location": {"min_length": 10},
        }
