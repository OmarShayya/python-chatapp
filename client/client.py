import socket
import threading

# Define the host and port number
HOST = 'localhost'
PORT = 8888

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Function to receive messages from the server
def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # If an error occurs, close the client socket
            client_socket.close()
            break

# Function to send messages to the server
def send():
    while True:
        message = input()
        client_socket.send(message.encode())

# Start two threads to receive and send messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()