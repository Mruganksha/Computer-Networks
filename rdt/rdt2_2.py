import random

expected_seq = 0

def checksum(data):
    return sum(ord(c) for c in data)

def make_packet(seq, data):
    return (seq, data, checksum(data))

def is_corrupt(packet):
    seq, data, check = packet
    return checksum(data) != check

def channel(packet):
    if random.random() < 0.3:
        print("Channel: Packet corrupted")
        seq, data, check = packet
        packet = (seq, "XXXX", check)

    return receiver(packet)

def receiver(packet):
    global expected_seq

    if is_corrupt(packet):
        print("Receiver: Corrupt packet")
        return expected_seq

    seq, data, _ = packet

    if seq == expected_seq:
        print("Receiver accepted:", data)
        expected_seq = 1 - expected_seq
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
                print("Wrong ACK -> Resend")

data = ["Hello", "Reliable", "Transfer"]

sender(data)