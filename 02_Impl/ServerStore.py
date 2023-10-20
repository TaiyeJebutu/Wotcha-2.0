import logging

from Store import  Store



class ServerStore(Store):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self._log_area = "ServerStore"
        self.logger.info(f"{self._log_area}: Creating ServerStore")

    def add(self, data):
        super().add(data)
        self.logger.info(f"{self._log_area}: Adding message to ServerStore")
