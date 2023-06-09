from server import Server

port = int(input('Enter the port number of Server: '))
server = Server(port)
server.start()
