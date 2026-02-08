import socket 
import json 
from root_dns import root_dns_db

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(5)

print("Root DNS Server started on port 5000...")

while True:
    conn, addr = server.accept()

    data = conn.recv(1024).decode()
    request = json.loads(data)

    domain = request["domain"]
    recursive = request["recursive"]

    print("\nRoot received request for:", domain)

    tld = domain.split(".")[-1]

    if tld in root_dns_db:
        tld_ip, tld_port = root_dns_db[tld]

        if not recursive:
            response = {
                "next_server_ip": tld_ip,
                "next_server_port": tld_port
            }
            conn.send(json.dumps(response).encode())

        else:
            tld_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tld_socket.connect((tld_ip, tld_port))
            tld_socket.send(json.dumps(request).encode())
            final_answer = tld_socket.recv(1024).decode()
            tld_socket.close()

            conn.send(final_answer.encode())

    else:
        conn.send(json.dumps({"error": "TLD not found"}).encode())

    conn.close()