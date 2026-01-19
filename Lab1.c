#include <stdio.h>
#include <math.h>

/* Function to print IP address from 32-bit integer */
void printIPAddress(unsigned int ipAddress) {
    printf("%u.%u.%u.%u",
           (ipAddress >> 24) & 255,
           (ipAddress >> 16) & 255,
           (ipAddress >> 8) & 255,
           ipAddress & 255);
}

/* Function to count number of 1 bits */
int countOneBits(unsigned int number) {
    int count = 0;
    while (number) {
        count += number & 1;
        number >>= 1;
    }
    return count;
}

int main() {

    unsigned int ipOctet[4];
    unsigned int maskOctet[4];

    unsigned int ipAddress = 0;
    unsigned int subnetMask = 0;

    printf("Enter IP Address: ");
    scanf("%u.%u.%u.%u",
          &ipOctet[0], &ipOctet[1], &ipOctet[2], &ipOctet[3]);

    printf("Enter Subnet Mask: ");
    scanf("%u.%u.%u.%u",
          &maskOctet[0], &maskOctet[1], &maskOctet[2], &maskOctet[3]);

    /* Convert IP and Subnet Mask to 32-bit form */
    for (int i = 0; i < 4; i++) {
        ipAddress = (ipAddress << 8) | ipOctet[i];
        subnetMask = (subnetMask << 8) | maskOctet[i];
    }

    /* Network and Broadcast Address */
    unsigned int networkID = ipAddress & subnetMask;
    unsigned int broadcastID = networkID | (~subnetMask);

    /* Bit calculations */
    int totalNetworkBits = countOneBits(subnetMask);
    int totalHostBits = 32 - totalNetworkBits;

    int addressesPerSubnet = pow(2, totalHostBits);
    int hostsPerSubnet = addressesPerSubnet - 2;

    /* Class identification */
    int defaultClassBits;
    if (ipOctet[0] <= 127)
        defaultClassBits = 8;
    else if (ipOctet[0] <= 191)
        defaultClassBits = 16;
    else
        defaultClassBits = 24;

    int borrowedBits = totalNetworkBits - defaultClassBits;
    int numberOfSubnets = pow(2, borrowedBits);

    printf("\nRESULTS: \n");
    printf("Number of Subnets: %d\n", numberOfSubnets);
    printf("Addresses per Subnet: %d\n", addressesPerSubnet);
    printf("Hosts per Subnet: %d\n", hostsPerSubnet);

    printf("\nNetwork ID: ");
    printIPAddress(networkID);

    printf("\nBroadcast ID: ");
    printIPAddress(broadcastID);

    printf("\n\nSubnet-wise Network and Broadcast IDs:\n");

    unsigned int subnetIncrement = addressesPerSubnet;

    for (int subnetIndex = 0; subnetIndex < numberOfSubnets; subnetIndex++) {

        unsigned int subnetNetworkID =
            networkID + (subnetIndex * subnetIncrement);

        unsigned int subnetBroadcastID =
            subnetNetworkID + subnetIncrement - 1;

        printf("\nSubnet %d\n", subnetIndex + 1);
        printf("Network ID: ");
        printIPAddress(subnetNetworkID);
        printf("\nBroadcast ID: ");
        printIPAddress(subnetBroadcastID);
        printf("\n");
    }

    return 0;
}
