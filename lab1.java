import java.util.Scanner;

public class SimpleSubnet {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        char ipClass;
        int defaultMask = 0;
        int cidr;
        int[] ip = new int[4];

        System.out.print("Select IP Class (A / B / C): ");
        ipClass = sc.next().charAt(0);

        if (ipClass == 'A' || ipClass == 'a') {
            System.out.println("Class A");
            System.out.println("IP Range: 1.0.0.0 to 126.255.255.255");
            defaultMask = 8;
        }
        else if (ipClass == 'B' || ipClass == 'b') {
            System.out.println("Class B");
            System.out.println("IP Range: 128.0.0.0 to 191.255.255.255");
            defaultMask = 16;
        }
        else if (ipClass == 'C' || ipClass == 'c') {
            System.out.println("Class C");
            System.out.println("IP Range: 192.0.0.0 to 223.255.255.255");
            defaultMask = 24;
        }
        else {
            System.out.println("Invalid Class");
            return;
        }

        System.out.println("Default Subnet Mask: /" + defaultMask);

        System.out.print("Enter IP Address: ");
        String ipAddress = sc.next();
        String[] parts = ipAddress.split("\\.");

        for (int i = 0; i < 4; i++) {
            ip[i] = Integer.parseInt(parts[i]);
        }

        System.out.print("Enter CIDR: ");
        cidr = sc.nextInt();

        if (cidr < defaultMask) {
            System.out.println("Invalid CIDR for selected class!");
            return;
        }

        int hostBits = 32 - cidr;
        int blockSize = (int) Math.pow(2, hostBits);

        int networkID = ip[3] - (ip[3] % blockSize);
        int broadcastID = networkID + blockSize - 1;

        int numberOfSubnets = (int) Math.pow(2, cidr - defaultMask);
        int hostsPerSubnet = blockSize - 2;

        System.out.println("\nNumber of Subnets: " + numberOfSubnets);
        System.out.println("Hosts per Subnet: " + hostsPerSubnet);

        System.out.println("\nNetwork ID: "
                + ip[0] + "." + ip[1] + "." + ip[2] + "." + networkID);

        System.out.println("Broadcast Address: "
                + ip[0] + "." + ip[1] + "." + ip[2] + "." + broadcastID);

        System.out.println("Valid Host Range: "
                + ip[0] + "." + ip[1] + "." + ip[2] + "." + (networkID + 1)
                + " to "
                + ip[0] + "." + ip[1] + "." + ip[2] + "." + (broadcastID - 1));

        sc.close();
    }
}
