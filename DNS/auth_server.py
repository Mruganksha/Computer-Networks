import socket 
import json 
from auth_dns import auth_dns_db

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5002))
server.listen(5)

print("Authoritative DNS Server started on port 5002...")

while True:
    conn, addr = server.accept()

    data = conn.recv(1024).decode()
    request = json.loads(data)

    domain = request["domain"]

    print("\nAuth server received request for:", domain)

    if domain in auth_dns_db:
        response = {
            "ip_address": auth_dns_db[domain]
        }
    else:
        response = {"error": "Record not found"}

    conn.send(json.dumps(response).encode())
    conn.close()