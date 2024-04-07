# opencanary_configurator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('status/', views.honeypot_status, name='honeypot_status'),
    path('enable_disable/<int:service_id>/', views.enable_disable_service, name='enable_disable_service'),
    path('logs/', views.live_logs, name='live_logs'),
    path('logs/http/', views.get_http_logs, name='http_logs'),
    path('logs/https/', views.get_https_logs, name='https_logs'),
]