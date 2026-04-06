def slow_start():
    cwnd = 1
    ssthresh = 16

    print(" Slow Start :")

    for i in range(1, 11):
        print(f"Round {i} -> cwnd = {cwnd}")

        if i == 7:
            print("Packet Loss Detected!")
            ssthresh = cwnd // 2
            print(f"New ssthresh = {ssthresh}")
            cwnd = 1
        elif cwnd < ssthresh:
            cwnd *= 2
        else:
            cwnd += 1


if __name__ == "__main__":
    slow_start()