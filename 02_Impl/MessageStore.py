import logging

from Store import Store



class MessageStore(Store):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self._log_area = "MessageStore"
        self.logger.info(f"{self._log_area}: Creating MessageStore")


    def add(self, data, _):
        super().add(data, _)
        self.logger.info(f"{self._log_area}: Adding message to MessageStore")
