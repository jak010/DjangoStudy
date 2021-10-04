from django.apps import AppConfig


class AppsigConfig(AppConfig):
    name = 'appsig'

    def ready(self):
        import appsig.handler