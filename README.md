# TCP Chat Room Project

This project is a TCP-based chat room application written in Python. It allows up to 5 clients to connect and communicate with each other in real-time.


## Features
- **TCP Protocol**: The chat room utilizes the TCP (Transmission Control Protocol) for reliable and ordered communication between the server and clients.

- **Multiple Clients**: The application is designed to handle up to 5 clients simultaneously. Each client can connect to the server and participate in the chat room.

- **Real-time Communication**: The chat room provides real-time communication between clients. Messages sent by one client are immediately broadcasted to all other connected clients.

- **Simple and Intuitive**: The chat room has a user-friendly interface, making it easy for clients to connect, send messages, and view the ongoing conversation.

---

## Usage
1. Start the server by running the `main_server.py` script.

2. Run the `main_client.py` script on up to 5 different machines or terminals to connect clients to the chat room.

3. Once connected, clients can start sending and receiving messages in real-time.

---

## Installation
To run this project on your local machine, follow these steps:

1. Clone the repository:

```bash
$ git clone https://github.com/your-username/tcp-chat-room.git
```
2. Change into the project directory:

```bash
$ cd tcp-chat-room
```
3. Run the `main_server.py` file and enter the port you want the chat to run
```bash
$ python3 main_server.py
Enter the port number of Server: 
```
4. Run the `main_client.py` file up to 5 times and enter your name and the same port that you entered for the server
```bash
$ python3 main_client.py
Enter your name: 
Enter the port you want to connect: 
```

![image](https://static.javatpoint.com/core/images/socket-programming.png)
