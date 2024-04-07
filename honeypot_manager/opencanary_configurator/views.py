import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HoneypotService

def honeypot_status(request):
    services = HoneypotService.objects.all()
    return render(request, 'honeypot_status.html', {'services': services})

def enable_disable_service(request, service_id):
    service = HoneypotService.objects.get(pk=service_id)
    service.is_enabled = not service.is_enabled
    service.save()
    return redirect('honeypot_status')

def live_logs(request):
    log_file_path = '/var/tmp/opencanary.log'
    logs = []

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                log_data = json.loads(line.strip())
                logs.append(log_data)
    except FileNotFoundError:
        pass

    return render(request, 'live_logs.html', {'logs': logs})

def get_http_logs(request):
    log_file_path = '/var/tmp/opencanary.log'
    http_logs = []

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                log_data = json.loads(line.strip())
                if log_data.get('dst_port') == 80:
                    http_logs.append(log_data)
    except FileNotFoundError:
        pass

    return render(request, 'http_logs.html', {'http_logs': http_logs})

def get_https_logs(request):
    log_file_path = '/var/tmp/opencanary.log'
    https_logs = []

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                log_data = json.loads(line.strip())
                if log_data.get('dst_port') == 443:
                    https_logs.append(log_data)
    except FileNotFoundError:
        pass

    return render(request, 'https_logs.html', {'https_logs': https_logs})


def dashboard(request):
    return render(request, 'dashboard.html')