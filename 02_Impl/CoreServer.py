import logging
import socket
from threading import Thread
from ServerStore import ServerStore
import _thread


class CoreServer:

    def __init__(self):
        self._store = ServerStore()
        self.logger = logging.getLogger(__name__)
        self._log_area = "CoreServer"
        self.logger.info(f"{self._log_area}: Creating CoreServer")
        self._translator = None
        self._thread = Thread(target=self.server_program)

    def start(self):
        self._thread.start()

    def handle_message(self, msg,addr):
        self.logger.info(f"{self._log_area}: Message Received -> {msg}")
        self._store.add(msg,addr)

    def on_new_client(self, client_socket, addr):
        client_socket.send(str(addr[1]).encode())
        while True:
            try:
                msg = client_socket.recv(1024).decode()

                if not msg:
                    continue
                thread = Thread(target=self.handle_message, args=(msg,addr))
                thread.start()
            except:
                break

        client_socket.close()

    def bind_sockets(self, port):
        host = socket.gethostname()
        port = port
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(10)

        while True:
            conn, address = server_socket.accept()  # accept new connection
            print("Connection from: " + str(address))
            self._translator.connections[address] = "bin"
            _thread.start_new_thread(self.on_new_client(conn, address))

    def server_program(self):
        # get the hostname
        host = socket.gethostname()

        ports = [5000,5001]

        for port in ports:
            _thread.start_new_thread(self.bind_sockets, (port,))


