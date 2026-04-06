import random

def selective_repeat(total_packets, window_size, loss_prob):

    transmissions = 0
    received = [False] * total_packets

    while not all(received):

        for i in range(total_packets):

            if not received[i]:

                transmissions += 1
                print("Sending packet", i)

                if random.random() < loss_prob:
                    print("Packet", i, "lost")
                else:
                    print("Packet", i, "received")
                    received[i] = True

    return transmissions


packets = 10
window = 4
loss = 0.3

total = selective_repeat(packets, window, loss)

print("\nTotal transmissions:", total)