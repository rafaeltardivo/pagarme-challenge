from django.apps import AppConfig


class BillingsConfig(AppConfig):
    name = 'billings'

    def ready(self):
        import billings.signals  # noqa
