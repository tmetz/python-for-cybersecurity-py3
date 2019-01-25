import socket

target_host = "www.google.com"
target_port = 80

# create a socket object - AF_INET means IPv4, and SOCK_STREAM means it's a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send data
string_to_send = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(string_to_send.encode())

# receive data
response = client.recv(4096).decode()

print (response)