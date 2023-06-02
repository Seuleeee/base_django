
import logging.config

from config.settings.base import LOGGING

logging.config.dictConfig(LOGGING)
logger = logging.getLogger("base_django_dev")

__all__ = ["logger"]