def tcp_reno():
    cwnd = 1
    ssthresh = 16

    print("\n=== TCP Reno ===")

    for i in range(1, 16):
        print(f"Round {i} -> cwnd = {cwnd}")

        if i == 8:
            print("3 Duplicate ACKs (Packet Loss)")
            ssthresh = cwnd // 2
            print(f"New ssthresh = {ssthresh}")
            cwnd = ssthresh  # fast recovery 

        elif cwnd < ssthresh:
            cwnd *= 2
        else:
            cwnd += 1

if __name__ == "__main__":
    tcp_reno()