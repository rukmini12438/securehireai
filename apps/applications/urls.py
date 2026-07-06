from django.urls import path
from .views import ApplyToJobView, MyApplicationsView, RecruiterApplicationsView, UpdateApplicationStatusView, dashboard_page, my_applications_page

urlpatterns = [
    path('apply/', ApplyToJobView.as_view(), name='apply-to-job'),
    path('mine/', MyApplicationsView.as_view(), name='my-applications'),
    path('recruiter/', RecruiterApplicationsView.as_view(), name='recruiter-applications'),
    path('<int:pk>/update-status/', UpdateApplicationStatusView.as_view(), name='update-status'),
    path('dashboard-page/', dashboard_page, name='dashboard-page'),
    path('my-applications-page/', my_applications_page, name='my-applications-page'),
]