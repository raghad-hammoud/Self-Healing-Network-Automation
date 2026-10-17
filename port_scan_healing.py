
import socket
import struct
import os
import time

ATTACKER_IP = "192.168.10.100"  
THRESHOLD = 10


s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

print("[*] Self-Healing Port Scan Detection Agent Started...")

syn_counter = 0
start_time = time.time()

while True:
    packet, _ = s.recvfrom(2048)
    
   
    ip_header = packet[14:34]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    
    protocol = iph[6]
    src_ip = socket.inet_ntoa(iph[8])
    
   
    if protocol == 6 and src_ip == ATTACKER_IP:
        tcp_header = packet[34:54]
        tcph = struct.unpack('!HHLLBBHHH', tcp_header)
        flags = tcph[5]


        if flags & 0x02:
            syn_counter += 1


            if syn_counter >= THRESHOLD:
                print("\n[!] ALERT: Port Scanning / SYN Attack Detected from IP: " + ATTACKER_IP)
                print("[!] SYN Packets Received: " + str(syn_counter))
                print("[+] SELF-HEALING ACTION Initiated...")


                os.system("sudo iptables -A INPUT -s " + ATTACKER_IP + " -j DROP")

                print("[v] SUCCESS: Attacker IP Blocked Successfully in Firewall!\n")
                
                syn_counter = 0
                time.sleep(5)

    if time.time() - start_time > 5:
        syn_counter = 0
        start_time = time.time()

