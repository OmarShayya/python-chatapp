# python-chatapp

This is a basic chat application built using Python and sockets. It allows multiple clients to connect to a server and chat with each other in real-time. The server listens for incoming connections, adds clients to a list, and starts a new thread for each client to handle their messages. When a client sends a message, it is broadcast to all other clients in the chatroom. The clients can communicate with each other until they disconnect from the server.

