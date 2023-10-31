import logging
from threading import Thread





class GUI:

    def __init__(self,core ):
        self._core = core
        self.logger = logging.getLogger(__name__)
        self._log_area = "GUI"
        self.logger.info(f"{self._log_area}: Creating GUI")



    def update_display(self,message):
        if message is not None:
            self.logger.info(f"{self._log_area}: Translated Message Is -> {message[0]}\n")


    def check_for_messages(self):
        while True:
            if not self._core.shutdown:
                message = self._core.translator._store.get()
                self.update_display(message)
            else:
                self.logger.info(f"{self._log_area}: Stopping GUI")
                break



    def start(self):
        thread = Thread(target=self.check_for_messages)
        thread.start()
        self.logger.info(f"{self._log_area}: Starting GUI")
