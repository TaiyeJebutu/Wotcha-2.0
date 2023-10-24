from Core import Core
from GUI import GUI
from Translator import Translator
import logging


def run():
    core = Core()
    gui = GUI(core)
    translator = Translator(core.server)
    gui._translator = translator

    core.start()
    gui.start()
    # while True:
    #
    #     key = input("\nEnter what you want to Translate: ")
    #
    #     if key.lower() == 's':
    #         break
    #     else:
    #         core.server.handle_message(key)






if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG,format='%(levelname)s:%(message)s')
    run()