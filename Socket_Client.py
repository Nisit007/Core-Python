# Import socket module
import socket

# Create socket object to connect
s = socket.socket()

# Define the port on which you want to connect
port = 1234

# connect to the server on local computer
s.connect(('192.168.43.147', port))

# receive data from the server
print(s.recv(1024))

# Close the connection
s.close()

