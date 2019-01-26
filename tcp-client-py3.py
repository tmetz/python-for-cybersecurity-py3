import socket

target_host = "www.google.com"
target_port = 80

# create a socket object - AF_INET means IPv4, and SOCK_STREAM means it's a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# For Python 3, the data must be sent as a bytes object, not a string.
# So we have to use .encode() and .decode() to convert back and forth.
# https://stackoverflow.com/questions/33003498/typeerror-a-bytes-like-object-is-required-not-str
# send data
string_to_send = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(string_to_send.encode())

# receive data
response = client.recv(4096).decode()

print (response)