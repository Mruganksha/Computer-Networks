import random
import time

expected_seq = 0

def checksum(data):
    return sum(ord(c) for c in data)

def make_packet(seq, data):
    return (seq, data, checksum(data))

def is_corrupt(packet):
    seq, data, check = packet
    return checksum(data) != check

def channel(packet):

    if random.random() < 0.2:
        print("Channel: Packet lost")
        return None

    if random.random() < 0.2:
        print("Channel: Packet corrupted")
        seq, data, check = packet
        packet = (seq, "XXXX", check)

    return receiver(packet)

def receiver(packet):
    global expected_seq

    if packet is None:
        return None

    if is_corrupt(packet):
        print("Receiver: Corrupt packet")
        return None

    seq, data, _ = packet

    if seq == expected_seq:
        print("Receiver received:", data)
        expected_seq = 1 - expected_seq
        return seq
    else:
        print("Receiver: Duplicate packet")
        return seq

def sender(data_list):
    seq = 0

    for data in data_list:

        packet = make_packet(seq, data)

        while True:
            print("\nSender sending seq", seq, ":", data)

            ack = channel(packet)

            if ack == seq:
                print("Sender received ACK", ack)
                seq = 1 - seq
                break
            else:
                print("Timeout / Wrong ACK -> Resend")
                time.sleep(1)

data = ["Hello", "Reliable", "Data", "Transfer"]

sender(data)