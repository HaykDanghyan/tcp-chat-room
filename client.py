import socket
import threading


class Client:
    def __init__(self, port: int, name: str):
        self.__port = port
        self.__host = socket.gethostbyname(socket.gethostname())
        self.__name = name
        self.__addr = (self.__host, self.__port)
        self.__socket: socket.socket = None

    def start(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect(self.__addr)
        self.__socket.send(self.__name.encode())
        welcome = self.__socket.recv(1024).decode()
        print(welcome)

        receiver = threading.Thread(target=self.receive_messages)
        receiver.start()

        self.send_message()

    def send_message(self):
        while True:
            message = input()
            self.__socket.send(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.__socket.recv(1024).decode()
                if message:
                    print(message)
                else:
                    self.__socket.close()
                    return
            except ConnectionResetError:
                self.__socket.close()
                return
