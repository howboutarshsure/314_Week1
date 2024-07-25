import socket
import sys

# Define the host and port to listen on
host = 'localhost'
port = 8222
address = (host, port)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind(address)

# Listen for incoming connections
server_socket.listen(5)

print("Listening for client . . .")

# Wait for a connection
conn, client_address = server_socket.accept()
print("Connected to client at ", client_address)

try:
    while True:
        # Receive the data in small chunks and retransmit it
        data = conn.recv(2048)
        if data:
            message = data.decode()
            print("Message received from client:")
            print(message + '\n')

            # Check if the received message is 'shutdown'
            if message.lower() == "shutdown":
                print("Shutdown message received. Shutting down server.")
                break

        else:
            # No more data from client, break the loop
            break

finally:
    # Clean up the connection
    conn.close()
    print("Connection closed.")
    server_socket.close()
    print("Server shut down.")
