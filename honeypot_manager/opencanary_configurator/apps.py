from django.apps import AppConfig

class OpencanaryConfiguratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'opencanary_configurator'

    def ready(self):
        import opencanary_configurator.signals  # Import signals module
