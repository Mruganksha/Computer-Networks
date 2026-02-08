import socket
import json

ROOT = ("127.0.0.1", 5000)
TLD = ("127.0.0.1", 5001)
AUTH = ("127.0.0.1", 5002)

def iterative_query(domain):
    request = {
        "domain": domain,
        "recursive": False
    }

    print("\n----- ITERATIVE QUERY START -----")

    # Step 1: Ask ROOT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ROOT)
    s.send(json.dumps(request).encode())
    response = json.loads(s.recv(1024).decode())
    print("From ROOT:", response)
    s.close()

    print("Going to TLD server:", TLD)

    # Step 2: Ask TLD
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(TLD)
    s.send(json.dumps(request).encode())
    response = json.loads(s.recv(1024).decode())
    print("From TLD:", response)
    s.close()

    print("Going to Auth server:", AUTH)

    # Step 3: Ask Authoritative
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(AUTH)
    s.send(json.dumps(request).encode())
    response = json.loads(s.recv(1024).decode())
    s.close()

    print("Final Answer:", response)


def recursive_query(domain):
    request = {
        "domain": domain,
        "recursive": True
    }

    print("\n----- RECURSIVE QUERY START -----")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(ROOT)
    s.send(json.dumps(request).encode())
    response = json.loads(s.recv(1024).decode())
    s.close()

    print("Final Answer (Recursive):", response)

iterative_query("www.example.com")
recursive_query("www.example.com")
