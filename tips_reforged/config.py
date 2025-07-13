from mcdreforged.api.all import PluginServerInterface
from pydantic import BaseModel


class PluginConfig(BaseModel):
    interval: float | list = [20, 30]


def config_checker(config: PluginConfig) -> PluginConfig:
    if not isinstance(config, PluginConfig):
        raise TypeError("Argument must be a PluginConfig instance!")
    _config = config.model_copy()
    match _config.interval:
        case float():
            pass  # already valid
        case list(itv):
            if len(itv) != 2:
                raise TypeError(
                    "If interval is a list, it must have exactly two float elements."
                )
            try:
                itv = [float(i) for i in itv]
            except ValueError:
                raise TypeError("Interval list must contain float-compatible values.")
            _config.interval = itv
        case other:
            try:
                _config.interval = float(other)
            except ValueError:
                raise TypeError(
                    "Invalid interval type, must be float or list of floats."
                )
    return _config


def config_loader(server: PluginServerInterface) -> PluginConfig:
    config: PluginConfig = server.load_config_simple(target_class=PluginConfig)  # type: ignore
    return config_checker(config)
