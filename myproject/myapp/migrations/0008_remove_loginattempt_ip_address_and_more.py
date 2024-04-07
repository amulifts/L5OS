# Generated by Django 5.0.3 on 2024-04-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_remove_loginattempt_ipv4_remove_loginattempt_ipv6_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loginattempt",
            name="ip_address",
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="ipv4_address",
            field=models.GenericIPAddressField(blank=True, null=True, protocol="IPv4"),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="ipv6_address",
            field=models.GenericIPAddressField(blank=True, null=True, protocol="IPv6"),
        ),
    ]
