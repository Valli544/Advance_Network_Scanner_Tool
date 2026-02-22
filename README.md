# Advanced Network Security and Scanning CLI Tool

> **DISCLAIMER:**  
> This tool is intended strictly for **authorized, ethical, and educational use only**.  
> Unauthorized scanning or misuse of this software is prohibited.

---

## 1. Project Description

The **Advanced Network Security and Scanning Command Line Tool** is a Python-based, menu-driven application developed to demonstrate practical concepts of computer networking and cybersecurity. The tool enables users to collect network-related information, perform controlled port scanning, discover devices within a local network, verify service availability, and maintain detailed activity logs.

This project is suitable for **academic submission**, **cybersecurity learning**, and **authorized network assessment** in controlled environments.

---

## 2. Key Features

- Network and system information retrieval  
- Multi-threaded localhost port scanning  
- Local Area Network (LAN) device discovery (ARP-based)  
- HTTP / HTTPS service availability checking  
- Bluetooth adapter status detection  
- Persistent event logging with timestamps  
- Cross-platform compatibility (Windows / Linux)

---

## 3. Technology Stack

- **Programming Language:** Python 3  
- **Application Type:** Command Line Interface (CLI)  
- **Networking Concepts:** TCP/IP, ARP, Socket Programming  
- **Optional Dependency:** Scapy (for LAN scanning)  
- **Version Control:** Git  

---

## 4. Project Structure

```
projectcybersecurity/
│
├── cybersecurity.py        # Main application source code
├── network_scan.log        # Generated log file
├── README.md               # Project documentation
```

---

## 5. System Requirements

### Hardware Requirements
- Desktop or Laptop Computer  
- Minimum 4 GB RAM  
- Active network interface  

### Software Requirements
- Windows or Linux Operating System  
- Python 3.x  
- Required Python libraries:
  - socket
  - uuid
  - requests
  - threading
  - subprocess
  - platform
- Optional:
  - scapy (`pip install scapy`)

---

## 6. Installation and Setup

### Step 1: Clone the Repository
```
git clone https://github.com/Valli544/Advance_Network_Scanner_Tool.git
cd Advance_Network_Scanner_Tool
```

### Step 2: Install Dependencies
```
pip install requests
pip install scapy   # Optional, required for LAN device discovery
```

---

## 7. Execution Instructions

Run the application using the following command:
```
python cybersecurity.py
```

The program presents an interactive menu allowing the user to select various network security operations.

---

## 8. Logging and Auditing

All major operations performed by the tool are recorded with timestamps in the log file:
```
network_scan.log
```

This feature supports auditing, troubleshooting, and review of tool usage.

---

## 9. Security and Ethical Considerations

- This tool must be used **only on systems and networks owned by or authorized to the user**
- No exploit development or attack mechanisms are implemented
- The developer assumes no responsibility for misuse of this software

---

## 10. Limitations

- Public IP detection requires internet connectivity  
- LAN discovery requires Scapy and appropriate privileges  
- Bluetooth detection is dependent on operating system support  
- Designed for small-scale and educational use cases  

---

## 11. Future Enhancements

- Exporting scan results to CSV / JSON formats  
- Detection of running service versions  
- Improved error handling and validation  
- Colored and enhanced CLI output  
- GUI-based implementation  

---

## 12. Author

**Valli**  
Cybersecurity and Networking Project  

---

## 13. License

This project is released for **educational and academic purposes only**.  
Modification and redistribution are permitted with proper attribution.
