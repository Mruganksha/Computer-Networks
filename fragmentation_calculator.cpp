#include <iostream>
using namespace std;

int main() {
    int totalSize, mtu, header;

    cout << "Enter Total Packet Size: ";
    cin >> totalSize;

    cout << "Enter MTU: ";
    cin >> mtu;

    cout << "Enter Header Size: ";
    cin >> header;

    int dataSize = totalSize - header;
    int maxDataPerFragment = mtu - header;

    maxDataPerFragment = (maxDataPerFragment / 8) * 8;

    int offset = 0;
    int fragmentNo = 1;

    cout << "\nFragmentation Details:\n";

    while (dataSize > 0) {
        int fragmentData;

        if (dataSize > maxDataPerFragment)
            fragmentData = maxDataPerFragment;
        else
            fragmentData = dataSize;

        cout << "\nFragment " << fragmentNo++ << ":\n";
        cout << "Data Size = " << fragmentData << endl;
        cout << "Offset = " << offset << endl;

        if (dataSize > maxDataPerFragment)
            cout << "MF = 1\n";  
        else
            cout << "MF = 0\n";  

        offset += fragmentData / 8;
        dataSize -= fragmentData;
    }

    return 0;
}