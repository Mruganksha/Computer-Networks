def tcp_tahoe():
    cwnd = 1
    ssthresh = 16

    print("\n=== TCP Tahoe ===")

    for i in range(1, 16):
        print(f"Round {i} -> cwnd = {cwnd}")

        if i == 8:
            print("Packet Loss Detected!")
            ssthresh = cwnd // 2
            print(f"New ssthresh = {ssthresh}")
            cwnd = 1  # always reset to 1

        elif cwnd < ssthresh:
            cwnd *= 2
        else:
            cwnd += 1

if __name__ == "__main__":
    tcp_tahoe()