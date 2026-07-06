from django.shortcuts import render
from django.db import models
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Job
from .serializers import JobSerializer
from .permissions import IsRecruiter


class JobCreateView(generics.CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = Job.objects.filter(is_active=True)
        search = self.request.query_params.get('search')
        location = self.request.query_params.get('location')
        job_type = self.request.query_params.get('job_type')

        if search:
            queryset = queryset.filter(
                models.Q(title__icontains=search) |
                models.Q(skills_required__icontains=search) |
                models.Q(company_name__icontains=search)
            )
        if location:
            queryset = queryset.filter(location__icontains=location)
        if job_type:
            queryset = queryset.filter(job_type=job_type)

        return queryset


def post_job_page(request):
    return render(request, 'jobs/post_job.html')


def browse_jobs_page(request):
    return render(request, 'jobs/browse_jobs.html')