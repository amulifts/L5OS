# Generated by Django 5.0.3 on 2024-04-03 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0019_alter_loginattempt_latitude_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="loginattempt",
            name="vpn",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]