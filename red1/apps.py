from django.apps import AppConfig


class Red1Config(AppConfig):
    name = 'red1'

    def ready(self):
        import red1.signals