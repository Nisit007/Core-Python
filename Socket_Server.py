# import socket module is an inbuilt
import socket
# To connect with socket
s = socket.socket()
# print this line when socket is successfully created
print("Socket success fully created")
# This is a port it's require to client side connect the server
port = 1234
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))

# put the socket into listening mode

s.listen(1024)
print("socket is listning")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.

    c, addr = s.accept()
    print("got connection from", addr)

    output = input("enter")
    c.sendall(output.encode('utf-8'))

    # Close the connection with client
    c.close()
