import socket

sender = input("Enter sender email: ")
receiver = input("Enter receiver email: ")
subject = input("Enter subject: ")
body = input("Enter message: ")

server = "localhost"
port = 1025

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server, port))

def recv():
    response = client_socket.recv(1024).decode()
    print(response)

def send(cmd):
    print("C:", cmd)
    client_socket.send((cmd + "\r\n").encode())

recv()  

send("HELO localhost")
recv()

send(f"MAIL FROM:<{sender}>")
recv()

send(f"RCPT TO:<{receiver}>")
recv()

send("DATA")
recv()

client_socket.send(f"Subject: {subject}\r\n".encode())
client_socket.send(f"\r\n{body}\r\n.\r\n".encode())
recv()

send("QUIT")
recv()

client_socket.close()

print("Mail sent successfully!")
