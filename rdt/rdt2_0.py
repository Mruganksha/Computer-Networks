#rdt 2.0 handles corrupted bit data

import random

def checksum(data):
    return sum(ord(c) for c in data)

def make_packet(data):
    return (data, checksum(data))

def is_corrupt(packet):
    data, check = packet
    return checksum(data) != check

def channel(packet):
    if random.random() < 0.3:
        print("Channel: Packet corrupted")
        data, check = packet
        packet = ("XXXX", check)

    return receiver(packet)

def receiver(packet):
    if is_corrupt(packet):
        print("Receiver: Corrupted packet -> NAK")
        return "NAK"
    else:
        data, _ = packet
        print("Receiver: Received:", data)
        return "ACK"

def sender(data):
    packet = make_packet(data)

    while True:
        print("\nSender sending:", data)
        response = channel(packet)

        if response == "ACK":
            print("Sender received ACK")
            break
        else:
            print("Sender received NAK -> Resending")

data_list = ["Hello", "Network", "Protocol"]

for data in data_list:
    sender(data)