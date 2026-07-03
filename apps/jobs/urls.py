from django.urls import path
from .views import JobCreateView, post_job_page

urlpatterns = [
    path('create/', JobCreateView.as_view(), name='job-create'),
    path('post-job-page/', post_job_page, name='post-job-page'),
]