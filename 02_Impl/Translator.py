import logging

from MessageStore import MessageStore
from CoreServer import CoreServer
from Filter import Filter
from threading import Thread


class Translator:

    def __init__(self, server: CoreServer):
        self._store = MessageStore()
        self._server = server
        self._shutdown = False
        self.logger = logging.getLogger(__name__)
        self._log_area = "Translator"
        self.logger.info(f"{self._log_area}: Creating Translator")

    def translate(self, message, _filter=Filter.bin):
        new_message = _filter(message)
        self.logger.info(f"{self._log_area}: Message Translated")
        self._store.add(new_message)

    def check_for_messages(self):
        while not self._shutdown:
            message = self._server._store.get()
            if message is not None:
                self.translate(message)

    def start(self):
        thread = Thread(target=self.check_for_messages)
        thread.start()
        self.logger.info(f"{self._log_area}: Starting Translator")
