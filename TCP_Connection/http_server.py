import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 5000))

server_socket.listen(1)
print("HTTP Server running on http://127.0.0.1:5000")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive HTTP request
    request = client_socket.recv(1024).decode()
    print("Request received:\n", request)

    # Prepare HTTP response
    response = """HTTP/1.1 200 OK
Content-Type: text/html

<html>
<head><title>My HTTP Server</title></head>
<body>
<h1>Welcome to My HTTP Server!</h1>
<p>This response was sent using raw TCP sockets.</p>
</body>
</html>
"""

    client_socket.send(response.encode())

    client_socket.close()
