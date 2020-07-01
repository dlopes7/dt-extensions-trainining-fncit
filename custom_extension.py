import logging

from ruxit.api.base_plugin import RemoteBasePlugin

log = logging.getLogger(__name__)


class CustomExtension(RemoteBasePlugin):

    def query(self, **kwargs):
        pass
