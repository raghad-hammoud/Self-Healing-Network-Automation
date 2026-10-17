# Self-Healing Network Infrastructure
## 👥 Project Team & Supervision
* **Students:** Raghad Mohammad Hammoud, Mariam Wadea Essa
* **Supervisor:** Dr. Eng. Ahmad Mahmoud Ahmad
* **Institution:** Latakia University - Faculty of Information Technology Engineering (Networks & Operating Systems Department)
* ## 📝 Project Overview
This project presents a closed-loop **Self-Healing Network Architecture** that integrates infrastructure redundancy (HSRP & OSPF) with autonomous Python software agents.
It is designed to detect and mitigate network threats (such as DoS floods, port scanning, and ARP spoofing) in real-time, ensuring High Availability and Service Continuity without manual intervention.
## 🛠️ Tech Stack & Simulation Environment
* **Simulation Platforms:** GNS3 (Cisco IOU) & VMware Workstation[cite: 11, 30]
* **Operating Systems:** Ubuntu Server (Web & Agent Host), Ubuntu Client, Kali Linux (Attacker Node)[cite: 11, 26, 45]
* **Languages & Automation:** Python (Scapy, Sockets, Subprocess)[cite: 11, 34]
* **Networking & Security Tools:** Wireshark, iptables, ApacheBench[cite: 11, 50]
* ## 📊 Tested Attack Scenarios & Automated Mitigation

| Attack Type | Target / Protocol | Detection Mechanism | Automated Response | MTTR (Response Time) |
| :--- | :--- | :--- | :--- | :--- |
| **DoS Flood Attack** | HTTP / ICMP | Concurrent requests threshold tracking | Dynamic `iptables` DROP rule injection | `< 50 ms` |
| **Port Scanning** | TCP SYN Scan (`Nmap`) | SYN packet threshold monitoring | Attacker IP immediate isolation | `< 50 ms` |
| **ARP Spoofing** | Layer 2 / Gateway | Real-time Gateway MAC validation | ARP table healing & Attacker IP block | `< 50 ms` |
