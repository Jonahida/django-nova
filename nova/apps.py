from django.apps import AppConfig

class NovaConfig(AppConfig):
    name = "nova"
    verbose_name = "Django Nova"

    def ready(self):
        import nova.signals  # noqa

