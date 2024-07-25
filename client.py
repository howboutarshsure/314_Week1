import random
import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8222))

for index in range(10):
    data = "test"
    print ("send to server: ", data)
    client_socket.send(data.encode())
    time.sleep(0.01)  # Example: Sending data every 0.01 seconds
