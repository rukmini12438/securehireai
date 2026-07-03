from django.shortcuts import render
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


def post_job_page(request):
    return render(request, 'jobs/post_job.html')