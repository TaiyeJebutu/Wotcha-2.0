import logging

from Stores.MessageStore import MessageStore
from CoreServer import CoreServer
from threading import Thread


class Translator:

    def __init__(self, server: CoreServer):
        self._store = MessageStore()
        self._server = server
        self._shutdown = False
        self.logger = logging.getLogger(__name__)
        self._log_area = "Translator"
        self.logger.info(f"{self._log_area}: Creating Translator")


    def translate(self, message):
        new_message = message.upper()
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
