#!/usr/bin/env python3
"""
ADVANCED NETWORK SECURITY CLI TOOL
-----------------------------------
Features:
1. Show Network Details
2. Scan Localhost Ports
3. Discover LAN Devices
4. Check HTTP/HTTPS Service
5. Bluetooth Status Check
6. View Logs
0. Exit

FOR AUTHORIZED USE ONLY.
"""

import socket
import uuid
import requests
import platform
import threading
import subprocess
import os
from datetime import datetime
from queue import Queue

# Optional scapy import for LAN scan
try:
    from scapy.all import ARP, Ether, srp
    SCAPY_AVAILABLE = True
except:
    SCAPY_AVAILABLE = False

LOG_FILE = "network_scan.log"


# ==============================
# Logging System
# ==============================

def log_event(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")


# ==============================
# Network Info Functions
# ==============================

def get_hostname():
    return socket.gethostname()


def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unable to fetch"


def get_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except:
        return "Unavailable"


def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))


# ==============================
# Localhost Port Scanner
# ==============================

def scan_port(port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex(("127.0.0.1", port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except:
        pass


def localhost_scan(start, end):
    print("\nScanning localhost ports...")
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
# LAN Device Discovery
        sock = socket.create_connection((host, port), timeout=3)
        request = f"HEAD / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        sock.send(request.encode())
        response = sock.recv(1024).decode(errors="ignore")
        sock.close()
        return response.split("\n")[0]
    except:
        return "No HTTP response"


# ==============================
# Bluetooth Status Check
# ==============================

def bluetooth_check():
    print("\nChecking Bluetooth availability...")

    if platform.system() == "Linux":
        try:
            result = subprocess.run(["hciconfig"], capture_output=True, text=True)
            if "hci" in result.stdout:
                return "Bluetooth adapter detected"
            else:
                return "No Bluetooth adapter found"
        except:

def menu():
    while True:
        print("\n" + "=" * 50)
        print(" ADVANCED NETWORK SECURITY CLI ")
        print("=" * 50)
        print("1️⃣  Show Network Details")
        print("2️⃣  Scan Localhost Ports")
        print("3️⃣  Discover LAN Devices")
        print("4️⃣  Check HTTP/HTTPS Service")
        print("5️⃣  Bluetooth Status Check")
        print("6️⃣  View Logs")
        print("0️⃣  Exit")
        print("=" * 50)

        choice = input("Select option: ")

        if choice == "1":
            show_network_info()

        elif choice == "2":
            start = int(input("Start port: "))
            end = int(input("End port: "))
            ports = localhost_scan(start, end)
            print("Open Ports:", ports)
            log_event(f"Scanned localhost ports {start}-{end}")

        elif choice == "3":
            local_ip = get_local_ip()
            subnet = get_subnet(local_ip)
            devices = scan_network(subnet)

            if devices:
                for ip, mac in devices:
                    print(f"IP: {ip}  MAC: {mac}")
            else:
                print("No devices found.")

            log_event("Scanned LAN devices")

        elif choice == "4":
            host = input("Enter host (e.g., 127.0.0.1): ")
            port = int(input("Enter port (80 or 443): "))
            response = check_http(host, port)
            print("Response:", response)
            log_event(f"Checked HTTP service on {host}:{port}")

        elif choice == "5":
            result = bluetooth_check()
            print(result)
            log_event("Checked Bluetooth status")

        elif choice == "6":
            show_logs()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid selection.")


# ==============================
# Main
# ==============================

if __name__ == "__main__":
    print("Authorized Use Only - Network CLI Tool")
    menu()            return "Bluetooth check failed"

    elif platform.system() == "Windows":
        try:
            result = subprocess.run(["powershell",
                                     "Get-PnpDevice -Class Bluetooth"],
                                    capture_output=True, text=True)
            print(f.read())
    else:
        print("No logs found.")


# ==============================
# CLI Menu (Button Style)
# ==============================
            if "Bluetooth" in result.stdout:
                return "Bluetooth device detected"
            else:
                return "No Bluetooth device found"
    print("Public IP:", get_public_ip())
    print("MAC Address:", get_mac_address())
    print("Operating System:", platform.system(), platform.release())

    log_event("Viewed Network Details")


def show_logs():
    if os.path.exists(LOG_FILE):
        print("\n--- Event Logs ---")
        with open(LOG_FILE, "r") as f:
        except:
            return "Bluetooth check failed"

    else:
        return "Bluetooth check not supported on this OS"


# ==============================
# Display Functions
# ==============================

def show_network_info():
    print("\n--- Network Details ---")
    print("Hostname:", get_hostname())
    print("Local IP:", get_local_ip())
# ==============================

def get_subnet(ip):
    parts = ip.split(".")
        devices.append((received.psrc, received.hwsrc))

    return devices


# ==============================
# HTTP / HTTPS Checker
# ==============================

def check_http(host, port):
    try:
    return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"


        print("Scapy not installed. Install with: pip install scapy")
        return []

    print(f"\nScanning network {network_range} ...")
    arp = ARP(pdst=network_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:

