import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 5000))

http_request = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"

client_socket.send(http_request.encode())

response = client_socket.recv(4096).decode()

print("Response from server:\n")
print(response)

client_socket.close()
