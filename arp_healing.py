
import socket
import struct
import os

REAL_GATEWAY_MAC = "ca:01:78:32:00:08"
GATEWAY_IP = "192.168.10.1"
ATTACKER_IP = "192.168.10.100"


s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

print("[*] Self-Healing ARP Agent Started (Socket Sniffer)...")

while True:
    packet, _ = s.recvfrom(2048)
    
   
    eth_header = packet[:14]
    eth_protocol = struct.unpack('!H', eth_header[12:14])[0]
    
    if eth_protocol == 0x0806:  # ARP Packet
        arp_header = packet[14:42]
        arp_data = struct.unpack('!HHBBH6s4s6s4s', arp_header)

        operation = arp_data[4]
        sender_mac = ":".join([format(b, '02x') for b in arp_data[5]])
        sender_ip = socket.inet_ntoa(arp_data[6])


        if operation == 2 and sender_ip == GATEWAY_IP and sender_mac.lower() != REAL_GATEWAY_MAC.lower():
            print("\n[!] ALERT: Malicious ARP Reply Detected from Fake Gateway!")
            print("[!] Spoofed MAC Detected: " + sender_mac)
            print("[+] SELF-HEALING ACTION Initiated...")


            os.system("sudo ip neighbor replace " + GATEWAY_IP + " lladdr " + REAL_GATEWAY_MAC + " dev ens33")


            os.system("sudo iptables -A INPUT -s " + ATTACKER_IP + " -j DROP")

            print("[v] SUCCESS: ARP Table Healed & Attacker IP Blocked!\n")

