import socket 
import json 
from tld_dns import tld_dns_db

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5001))
server.listen(5)

print("TLD DNS Server .com started on port 5001...")

while True:
    conn, addr = server.accept()

    data = conn.recv(1024).decode()
    request = json.loads(data)

    domain = request["domain"]
    recursive = request["recursive"]

    print("\nTLD received request for:", domain)

    base_domain = ".".join(domain.split(".")[-2:])

    if base_domain in tld_dns_db:
        auth_ip, auth_port = tld_dns_db[base_domain]

        if not recursive:
            response = {
                "next_server_ip": auth_ip,
                "next_server_port": auth_port
            }
            conn.send(json.dumps(response).encode())

        else:
            auth_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            auth_socket.connect((auth_ip, auth_port))
            auth_socket.send(json.dumps(request).encode())
            final_answer = auth_socket.recv(1024).decode()
            auth_socket.close()

            conn.send(final_answer.encode())

    else:
        conn.send(json.dumps({"error": "Domain not found"}).encode())

    conn.close()