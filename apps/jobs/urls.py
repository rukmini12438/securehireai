from django.urls import path
from .views import JobCreateView, JobListView, post_job_page, browse_jobs_page

urlpatterns = [
    path('create/', JobCreateView.as_view(), name='job-create'),
    path('list/', JobListView.as_view(), name='job-list'),
    path('post-job-page/', post_job_page, name='post-job-page'),
    path('browse-jobs-page/', browse_jobs_page, name='browse-jobs-page'),
]