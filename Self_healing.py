import time
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
from collections import defaultdict

ip_requests = defaultdict(list)
BLOCKED_IPS = set()

class SelfHealingHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        now = time.time()

        ip_requests[client_ip] = [t for t in ip_requests[client_ip] if now - t < 5]
        ip_requests[client_ip].append(now)

        if len(ip_requests[client_ip]) > 15 and client_ip not in BLOCKED_IPS:
            print("\n[!] ALERT: DoS Attack detected from IP: " + str(client_ip))
            print("[+] SELF-HEALING ACTION: Blocking IP via iptables...")
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", str(client_ip), "$
            BLOCKED_IPS.add(client_ip)
            print("[v] SUCCESS: IP blocked successfully. Network auto-recovered!\n")

        super().do_GET()

if name == 'main':
    print("==================================================")
    print("  Self-Healing HTTP Web Server Agent Running...   ")
    print("==================================================")
    server = HTTPServer(('0.0.0.0', 80), SelfHealingHandler)
    server.serve_forever()