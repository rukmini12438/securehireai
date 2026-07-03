from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    posted_by_username = serializers.CharField(source='posted_by.username', read_only=True)

    class Meta:
        model = Job
        fields = (
            'id', 'title', 'company_name', 'location', 'job_type',
            'description', 'skills_required', 'salary_min', 'salary_max',
            'is_active', 'posted_by', 'posted_by_username', 'created_at',
        )
        read_only_fields = ('posted_by', 'created_at')