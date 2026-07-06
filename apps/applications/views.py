from django.shortcuts import render
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Application
from .serializers import ApplicationSerializer, ApplicationStatusUpdateSerializer
from .permissions import IsCandidate


class ApplyToJobView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsCandidate]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        job = serializer.validated_data.get('job')
        if Application.objects.filter(job=job, candidate=self.request.user).exists():
            raise ValidationError("You've already applied to this job.")
        serializer.save(candidate=self.request.user)


class MyApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsCandidate]

    def get_queryset(self):
        return Application.objects.filter(candidate=self.request.user)


class RecruiterApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(job__posted_by=self.request.user)


class UpdateApplicationStatusView(generics.UpdateAPIView):
    serializer_class = ApplicationStatusUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(job__posted_by=self.request.user)


def dashboard_page(request):
    return render(request, 'applications/dashboard.html')


def my_applications_page(request):
    return render(request, 'applications/my_applications.html')