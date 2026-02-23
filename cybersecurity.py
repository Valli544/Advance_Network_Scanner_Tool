#!/usr/bin/env python3
"""
ADVANCED NETWORK SECURITY CLI TOOL
FOR AUTHORIZED USE ONLY
"""

import socket
import uuid
import requests
import platform
import threading
import subprocess
import os
from datetime import datetime

# Optional scapy import
try:
    from scapy.all import ARP, Ether, srp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

LOG_FILE = "network_scan.log"


# ==============================
# Logging
# ==============================

def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")


# ==============================
# Network Info
# ==============================

def get_hostname():
    return socket.gethostname()


def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unavailable"


def get_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except:
        return "Unavailable"


def get_mac_address():
    mac = uuid.getnode()
    return ":".join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))


def show_network_info():
    print("\n--- Network Details ---")
    print("Hostname:", get_hostname())
    print("Local IP:", get_local_ip())
    print("Public IP:", get_public_ip())
    print("MAC Address:", get_mac_address())
    print("OS:", platform.system(), platform.release())
    log_event("Viewed network details")


# ==============================
# Localhost Port Scanner
# ==============================

def scan_port(port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        if sock.connect_ex(("127.0.0.1", port)) == 0:
            open_ports.append(port)
        sock.close()
    except:
        pass


def localhost_scan(start, end):
    open_ports = []
    threads = []

    for port in range(start, end + 1):
        t = threading.Thread(target=scan_port, args=(port, open_ports))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return sorted(open_ports)


# ==============================
# LAN Discovery
# ==============================

def get_subnet(ip):
    parts = ip.split(".")
    return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"


def scan_network(network_range):
    if not SCAPY_AVAILABLE:
        print("Scapy not available")
        return []

    arp = ARP(pdst=network_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]
    devices = []

    for _, received in result:
        devices.append((received.psrc, received.hwsrc))

    return devices


# ==============================
# HTTP / HTTPS Check
# ==============================

def check_http(host, port):
    try:
        sock = socket.create_connection((host, port), timeout=3)
        request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\n\r\n"
        sock.send(request.encode())
        response = sock.recv(1024).decode(errors="ignore")
        sock.close()
        return response.split("\n")[0]
    except:
        return "No HTTP response"


# ==============================
# Bluetooth Check
# ==============================

def bluetooth_check():
    if platform.system() == "Linux":
        try:
            output = subprocess.getoutput("hciconfig")
            if "hci" in output:
                return "Bluetooth adapter detected"
            else:
                return "No Bluetooth adapter found"
        except:
            return "Bluetooth check failed"
    else:
        return "Bluetooth not supported on this OS"


# ==============================
# Logs
# ==============================

def show_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            print("\n--- Logs ---")
            print(f.read())
    else:
        print("No logs found")


# ==============================
# Menu
# ==============================

def menu():
    while True:
        print("\n" + "=" * 50)
        print(" ADVANCED NETWORK SECURITY CLI ")
        print("=" * 50)
        print("1. Show Network Details")
        print("2. Scan Localhost Ports")
        print("3. Discover LAN Devices")
        print("4. Check HTTP/HTTPS Service")
        print("5. Bluetooth Status Check")
        print("6. View Logs")
        print("0. Exit")
        print("=" * 50)

        choice = input("Select option: ")

        if choice == "1":
            show_network_info()

        elif choice == "2":
            start = int(input("Start port: "))
            end = int(input("End port: "))
            ports = localhost_scan(start, end)
            print("Open Ports:", ports)
            log_event(f"Scanned ports {start}-{end}")

        elif choice == "3":
            subnet = get_subnet(get_local_ip())
            devices = scan_network(subnet)
            for ip, mac in devices:
                print(f"{ip}  {mac}")
            log_event("LAN scan performed")

        elif choice == "4":
            host = input("Host: ")
            port = int(input("Port: "))
            print(check_http(host, port))
            log_event(f"HTTP check {host}:{port}")

        elif choice == "5":
            print(bluetooth_check())
            log_event("Bluetooth checked")

        elif choice == "6":
            show_logs()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# ==============================
# Main
# ==============================

if __name__ == "__main__":
    print("Authorized Use Only - Network CLI Tool")
    menu()
