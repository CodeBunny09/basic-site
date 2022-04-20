from django.urls import path
from . import views

app_name = "stats"
urlpatterns = [
    path('organization-stats', views.organization_stats, name="organization-stats"),
    path('organization-stats/<id>', views.organization_stats, name="organization-stats"),
]