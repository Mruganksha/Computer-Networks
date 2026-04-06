def aimd():
    cwnd = 16

    print("\n=== AIMD ===")

    for i in range(1, 11):
        print(f"Round {i} -> cwnd = {cwnd}")

        if i == 6:
            print("Packet Loss Detected!")
            cwnd = cwnd // 2  
        else:
            cwnd += 1

if __name__ == "__main__":
    aimd()