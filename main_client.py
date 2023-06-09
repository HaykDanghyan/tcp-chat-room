from client import Client

name = input('Enter your name: ')
port = int(input('Enter the port you want to connect: '))
client = Client(port, name)
client.start()