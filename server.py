import socket
import threading


class Server:
    def __init__(self, port: int):
        self.__port = port
        self.__host = socket.gethostbyname(socket.gethostname())
        self.__addr = (self.__host, self.__port)
        self.__socket = None
        self.__lock = threading.Lock()
        self.__clients = []

    def start(self):
        print(f"Chat server started on {self.__host}:{self.__port}")
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind(self.__addr)
        self.__socket.listen(5)
        while True:
            client_sock, client_addr = self.__socket.accept()
            print(f"New client connected: {client_addr[0]}:{client_addr[1]}")

            self.__lock.acquire()
            self.__clients.append(client_sock)
            self.__lock.release()

            thread = threading.Thread(target=self.handle_client, args=(client_sock,))
            thread.start()

    def handle_client(self, client_sock: socket.socket):
        name = client_sock.recv(1024).decode()
        welcome_message = f"Welcome, {name}!"
        client_sock.send(welcome_message.encode())
        print(f"{name} joined the chat.")

        while True:
            try:
                message = client_sock.recv(1024).decode()
                if message:
                    print(f'{name} : {message}')
                    self.__lock.acquire()
                    for sock in self.__clients:
                        if sock != client_sock:
                            sock.send(f'{name}: {message}'.encode())
                    self.__lock.release()
                else:
                    self.__lock.acquire()
                    self.__clients.remove(client_sock)
                    self.__lock.release()
                    print(f"{name} left the chat.")
                    for sock in self.__clients:
                        if sock != client_sock:
                            sock.send(f'{name} left the chat')
                    client_sock.close()
                    return
            except ConnectionResetError:
                self.__lock.acquire()
                self.__clients.remove(client_sock)
                self.__lock.release()
                print(f"{name} left the chat.")
                client_sock.close()
                return

    def stop(self):
        if self.__socket:
            self.__socket.close()

        for client_socket in self.__clients:
            client_socket.close()

        print("Chat server stopped")
