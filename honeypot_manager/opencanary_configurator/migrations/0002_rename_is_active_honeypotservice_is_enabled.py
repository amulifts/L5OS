# Generated by Django 5.0.3 on 2024-03-30 11:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("opencanary_configurator", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="honeypotservice",
            old_name="is_active",
            new_name="is_enabled",
        ),
    ]
