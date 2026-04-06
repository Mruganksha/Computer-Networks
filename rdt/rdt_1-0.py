# rdt1.0 - Perfect channel (no loss, no corruption)

def sender(data):
    print("Sender sends:", data)
    channel(data)

def channel(packet):
    receiver(packet)

def receiver(packet):
    print("Receiver received:", packet)
    print("Data delivered successfully\n")

data_list = ["Hello", "Networking", "RDT Protocol"]

for data in data_list:
    sender(data)