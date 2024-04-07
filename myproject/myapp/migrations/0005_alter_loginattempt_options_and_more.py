# Generated by Django 5.0.3 on 2024-04-01 20:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_loginattempt_country_loginattempt_path_requested_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="loginattempt",
            options={"verbose_name_plural": "Login Attempts"},
        ),
        migrations.RenameField(
            model_name="loginattempt",
            old_name="path_requested",
            new_name="browser",
        ),
        migrations.RemoveField(
            model_name="loginattempt",
            name="ip_address",
        ),
        migrations.RemoveField(
            model_name="loginattempt",
            name="success",
        ),
        migrations.RemoveField(
            model_name="loginattempt",
            name="username",
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="city",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="ipv4",
            field=models.GenericIPAddressField(blank=True, null=True, protocol="IPv4"),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="ipv6",
            field=models.GenericIPAddressField(blank=True, null=True, protocol="IPv6"),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="isp",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=15, max_digits=18, null=True
            ),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, geography=True, null=True, srid=4326
            ),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="longitude",
            field=models.DecimalField(
                blank=True, decimal_places=15, max_digits=18, null=True
            ),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="platform",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="loginattempt",
            name="state",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="loginattempt",
            name="user_agent",
            field=models.TextField(blank=True, null=True),
        ),
    ]
