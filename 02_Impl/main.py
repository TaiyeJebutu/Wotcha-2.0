from Core import Core
from GUI import GUI
from Translator import Translator
import logging
from threading import Thread

def set_decoder():
    key = input("Enter <ip>-<port>-<decoder>"
                " or cancel to go back -->")

    if key.lower() != "cancel":
        try:
            params = key.split(sep = '-')
            print(f"You have chosen to use the [{params[2]}] decoder for the client with the ip {params[0]} and port"
                  f" {params[1]}\n")
            connection_key = tuple([params[0],int(params[1])])
            core.translator.connections[connection_key] = params[2]
        except Exception as e:
            pass
    else:
        pass

def get_decoder():
    print("Currently loaded decoders:\n")
    for key, value in core.translator.connections.items():
        print(f"{key}:{value}")
    print("\n")

def open_port():
    key = input("Port to open -> ")
    try:
        thread = Thread(target = core.server.bind_sockets, args= (int(key),))
        thread.start()
    except Exception as e:
        pass


def run():


    while True:

        print("----------System Running----------, press h for help")

        key = input("-->")

        if key.lower() == "set decode":
            set_decoder()
        if key.lower() == "get decoders":
            get_decoder()
        if key.lower() == "open port":
            open_port()
        if key.lower() == "shutdown":
            print("Shutting the system down ....")
            core.stop()
            break
        else:
            print(f"--------HELP--------\n"
                  f"set decode  : set the decode \n"
                  f"get decoders: get the decoders\n"
                  f"shutdown    : shutdown the system\n"
                  f"open port   : Open a port"
                  f"help        : show help menu")





if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG,format='%(levelname)s:%(message)s')

    core = Core()
    gui = GUI(core)
    translator = Translator(core.server)
    gui._translator = translator
    core.translator = translator
    core.server._translator = translator

    core.start()
    gui.start()

    run()