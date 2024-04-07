from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.login_view, name='capture_ip'),
    # path('map/', views.map_view, name='map'),
    path('login_attempts/', views.list_login_attempts, name='list_login_attempts'),
    path('redirect_to_map/', views.redirect_to_map, name='redirect_to_map'),  # For the latest or first entry
    # If you need to match the pattern manually with re_path
    re_path(r'^redirect_to_map/(?P<unique_number>[a-f0-9]+)/$', views.redirect_to_map, name='redirect_to_map')

]



# This presentation explores the Eternal Blue exploit, a major flaw in Microsoft's SMB protocol used in severe ransomware attacks like WannaCry and NotPetya. We'll look at its origins, how it works, and its effects on global cybersecurity. The presentation also covers implementation of this vulnerability in hack the box using metasploit.