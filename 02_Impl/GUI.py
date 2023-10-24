import logging
from threading import Thread




class GUI:

    def __init__(self,core ):
        self._core = core
        self._shutdown = False
        self.logger = logging.getLogger(__name__)
        self._log_area = "GUI"
        self.logger.info(f"{self._log_area}: Creating GUI")



    def update_display(self,message):
        if message is not None:
            self.logger.info(f"{self._log_area}: Translated Message Is -> {message}\n")


    def check_for_messages(self):
        while not self._shutdown:
            message = self._core.translator._store.get()
            self.update_display(message)

    def start(self):
        thread = Thread(target=self.check_for_messages)
        thread.start()
        self.logger.info(f"{self._log_area}: Starting GUI")
