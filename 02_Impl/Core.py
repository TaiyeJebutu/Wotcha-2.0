import logging
from threading import Thread

from GUI import  GUI
from Translator import Translator
from CoreServer import CoreServer


class Core:


    def __init__(self):

        self.server = CoreServer()
        self.translator = Translator(server=self.server)
        self.logger = logging.getLogger(__name__)
        self._log_area = "Core"
        self.logger.info(f"{self._log_area}: Creating Core")

    def start(self):
        self.translator.start()

