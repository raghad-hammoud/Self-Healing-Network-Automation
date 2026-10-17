# Self-Healing Network Infrastructure

## 👥 Project Team & Supervision

* **Students:** Raghad Mohammad Hammoud, Mariam Wadea Essa
* **Supervisor:** Dr. Eng. Ahmad Mahmoud Ahmad
* **Institution:** Lattakia University - Faculty of Information Technology Engineering (Networks & Operating Systems Department)

---

## 📝 Project Overview

This project presents a closed-loop **Self-Healing Network Architecture** that integrates infrastructure redundancy (HSRP & OSPF) with autonomous Python software agents. It is designed to detect and mitigate network threats (such as DoS floods, port scanning, and ARP spoofing) in real-time, ensuring High Availability and Service Continuity without manual intervention.

---

## 🛠 Tech Stack & Simulation Environment

* **Simulation Platforms:** GNS3 (Cisco IOU) & VMware Workstation.
* **Operating Systems:** Ubuntu Server (Web & Agent Host), Ubuntu Client, Kali Linux (Attacker Node).
* **Languages & Automation:** Python (Scapy, Sockets, Subprocess).
* **Networking & Security Tools:** Wireshark, iptables, ApacheBench.

---

## 📊 Tested Attack Scenarios & Automated Mitigation

| Attack Type | Target / Protocol | Detection Mechanism | Automated Response | Execution Time (Mitigation Latency) |
| :--- | :--- | :--- | :--- | :--- |
| **DoS Flood Attack** | HTTP / ICMP | Concurrent requests threshold tracking | Dynamic `iptables` DROP rule injection | Instantaneous (`< 50 ms` via script) |
| **Port Scanning** | TCP SYN Scan (`Nmap`) | SYN packet threshold monitoring | Attacker IP immediate isolation | Instantaneous (`< 50 ms` via script) |
| **ARP Spoofing** | Layer 2 / Gateway | Real-time Gateway MAC validation | ARP table healing & Attacker IP block | Instantaneous (`< 50 ms` via script) |

> **Note on Response Time:** The response time (`< 50 ms`) represents the internal execution latency between threat detection by the Python monitoring script and the dynamic application of the `iptables` block rule at the Linux kernel level.

---

## ⚙️ Prerequisites & Configuration

Before running the security scripts, ensure the environment meets the following requirements:
* **Dependencies:** Python 3.x, `scapy`, `iptables`, and `net-tools` (`sudo apt install iptables net-tools`).
* **Environment Setup:** Execute scripts on the designated Ubuntu Web/Agent Server with `root` / `sudo` privileges to allow `iptables` rules injection.

> **Configuration Note:** Key variables (such as target Interface `eth0`, Gateway IP/MAC, and Detection Thresholds) are currently localized within each script header (`self_healing.py`, `arp_healing.py`, `port_scan_healing.py`). Modify these parameters to fit your specific network subnet before deployment.

---

## 🧪 Usage & Testing

1. **Deploy Network Topology:** Launch the GNS3 topology using `Last_one.gns3` and boot the VMware nodes.
2. **Execute Agent Scripts:** Run the mitigation script on the server node:
   ```bash
   sudo python3 self_healing.py
Simulate Attacks: From the Kali Linux node, initiate an attack (e.g., HTTP flood via ab or SYN scan via nmap).

Verify Mitigation: Inspect active iptables DROP rules:

Bash
sudo iptables -L -n -v
---
⚠️Architectural Limitations & Future Scope
This project serves as an academic proof-of-concept for network-aware reactive defense. Key known limitations and planned enhancements include:

Static Thresholding: Current detection relies on fixed packet/request thresholds. Future enhancement: Incorporating dynamic anomaly detection using Machine Learning (AI-NIDS).

Mitigation Latency vs. Full Recovery: The < 50 ms metric strictly reflects script execution to iptables rule injection time. Future enhancement: Implementing automated health-check loops to verify service recovery post-mitigation.
