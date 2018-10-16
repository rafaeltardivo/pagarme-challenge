from django.apps import AppConfig


class WalletsConfig(AppConfig):
    name = 'wallets'

    def ready(self):
        import wallets.signals  # noqa
