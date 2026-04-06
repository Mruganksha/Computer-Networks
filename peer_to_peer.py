import socket
import threading

def receive(conn):
    while True:
        try:
            message = conn.recv(1024).decode()
            print("\nFriend:", message)
        except:
            break

def start_server(port):
    server = socket.socket()
    server.bind(("0.0.0.0", port))
    server.listen(1)
    print("Waiting for connection...")
    conn, addr = server.accept()
    print("Connected to", addr)

    threading.Thread(target=receive, args=(conn,), daemon=True).start()

    while True:
        msg = input("You: ")
        conn.send(msg.encode())

def connect_to_peer(ip, port):
    client = socket.socket()
    client.connect((ip, port))
    print("Connected to friend")

    threading.Thread(target=receive, args=(client,), daemon=True).start()

    while True:
        msg = input("You: ")
        client.send(msg.encode())

choice = input("Type 's' for server or 'c' for client: ")

if choice == "s":
    port = int(input("Enter port: "))
    start_server(port)

elif choice == "c":
    ip = input("Enter friend's IP: ")
    port = int(input("Enter friend's port: "))
    connect_to_peer(ip, port)
