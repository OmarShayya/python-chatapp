import socket
import threading

# Define the host and port number
HOST = 'localhost'
PORT = 8888

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket object to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}...")

# Create an empty list to store clients
clients = []

# Function to broadcast messages to all clients
def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

# Function to handle a client's messages
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except:
            # If an error occurs, remove the client from the list of clients
            clients.remove(client_socket)
            print(f"Client disconnected from {client_address[0]}:{client_address[1]}")
            break

# Accept incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Client connected from {client_address[0]}:{client_address[1]}")

    # Add the client to the list of clients
    clients.append(client_socket)

    # Send a welcome message to the client
    client_socket.send("Welcome to the chatroom!".encode())

    # Start a new thread to handle the client's messages
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()