# Generated by Django 5.0.3 on 2024-04-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0016_loginattempt_region_loginattempt_timezone"),
    ]

    operations = [
        migrations.AddField(
            model_name="loginattempt",
            name="is_vpn",
            field=models.BooleanField(default=False),
        ),
    ]
