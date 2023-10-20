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
        thread = Thread(target=self.server_program)
        thread.start()

    def handle_message(self, msg):
        self.logger.info(f"{self._log_area}: Message Received -> {msg}")
        self._store.add(msg)

    def on_new_client(self, client_socket, addr):
        while True:
            try:
                msg = client_socket.recv(1024).decode()
                if not msg:
                    continue
                thread = Thread(target=self.handle_message, args=(msg,))
                thread.start()
            except:
                break

        client_socket.close()

    def server_program(self):
        # get the hostname
        host = socket.gethostname()
        port = 5000  # initiate port no above 1024

        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen(10)
        while True:
            conn, address = server_socket.accept()  # accept new connection
            print("Connection from: " + str(address))
            _thread.start_new_thread(self.on_new_client(conn, address))

        # while True:
        #     # receive data stream. it won't accept data packet greater than 1024 bytes
        #     data = conn.recv(1024).decode()
        #     if not data:
        #         # if data is not received break
        #         continue
        #     thread = Thread(target=self.handle_message, args=(data,))
        #     thread.start()
        #
        # conn.close()  # close the connection
