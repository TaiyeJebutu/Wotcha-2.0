import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5001  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = ''

    while message.lower().strip() != 'bye':



        message = client_socket.recv(1024).decode()
        print(f"Designated Port: {message}")

        message = input(" -> ")  # again take input
        client_socket.send(message.encode())  # send message

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()