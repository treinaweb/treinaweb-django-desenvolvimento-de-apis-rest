from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from core.paginations import TWJobsPagination

from .models import Job
from .serializers import JobSerializer
from .filters import JobFilterSet


class JobList(APIView):
    def get(self, request):
        paginator = TWJobsPagination()
        qs = Job.objects.filter(is_active=True)
        filter = JobFilterSet(request.GET, queryset=qs)
        jobs = paginator.paginate_queryset(filter.qs, request)
        serializer = JobSerializer(jobs, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class JobDetail(APIView):
    def __get_object(self, pk):
        return get_object_or_404(Job, pk=pk, is_active=True)

    def get(self, request, pk):
        job = self.__get_object(pk)
        serializer = JobSerializer(job, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        job = self.__get_object(pk)
        serializer = JobSerializer(job, data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        job = self.__get_object(pk)
        job.is_active = False
        job.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
