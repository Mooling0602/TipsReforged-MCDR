from mcdreforged.api.all import PluginServerInterface
from tips_reforged.config import config_loader


def on_load(server: PluginServerInterface, _prev_module):
    config = config_loader(server)
    server.logger.info(config.interval)
