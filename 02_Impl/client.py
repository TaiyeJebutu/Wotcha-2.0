import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = ''
    wait_for_response = True

    while message.lower().strip() != 'bye':


        if wait_for_response:
            message = client_socket.recv(1024).decode()
            print(f"Designated Port: {message}")
            wait_for_response = False

        message = input(" -> ")  # again take input
        client_socket.send(message.encode())  # send message

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()