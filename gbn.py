import random

def gobackn(total_packets, window_size, loss_prob):

    base = 0
    transmissions = 0

    while base < total_packets:

        print("\nWindow starting at packet", base)

        for i in range(base, min(base + window_size, total_packets)):

            transmissions += 1
            print("Sending packet", i)

            if random.random() < loss_prob:
                print("Packet", i, "lost!")
                break

        else:
            base += window_size
            continue

        base = i

    return transmissions


packets = 10
window = 4
loss = 0.3

total = gobackn(packets, window, loss)

print("\nTotal transmissions:", total)