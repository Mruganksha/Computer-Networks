import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 12345))

server_socket.listen(1)
print("Server is waiting for a connection...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Receive data from client
data = client_socket.recv(1024).decode()
print("Received from client:", data)

# Send response back to client
response = "Hello from Server!"
client_socket.send(response.encode())

client_socket.close()
server_socket.close()
