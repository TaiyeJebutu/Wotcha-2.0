import logging
from threading import Thread

from GUI import  GUI
from Translator import Translator
from CoreServer import CoreServer


class Core:


    def __init__(self):

        self.server = CoreServer()
        self.translator = None
        self.logger = logging.getLogger(__name__)
        self._log_area = "Core"
        self.shutdown = False
        self.logger.info(f"{self._log_area}: Creating Core")

    def start(self):
        self.server.start()
        self.translator.start()

    def stop(self):
        self.shutdown = True
        self.server.stop()
        self.translator.stop()

