# Python Network Socket Port Scanner

## Overview

The **Python Network Socket Port Scanner** is a simple network security tool developed using Python's built-in `socket` module. The program scans a target hostname or IP address for common open TCP ports, attempts to retrieve service banners when available, and displays a scan report.

This project demonstrates the fundamentals of network programming, TCP socket communication, and port scanning.

## Features

* Scan a target hostname or IP address
* Automatically resolve hostnames to IP addresses
* Scan commonly used TCP ports
* Detect open ports
* Identify common network services
* Attempt to retrieve service banners (when available)
* Display a summary report of open ports
* Handle invalid hostnames gracefully

## Technologies Used

* Python 3
* `socket` module (built-in)

## Project Structure

```text
Python-Network-Socket-Port-Scanner/
│
├── port_scanner.py
└── README.md
```

## Common Ports Scanned

| Port | Service              |
| ---: | -------------------- |
|   20 | FTP (Data)           |
|   21 | FTP                  |
|   22 | SSH                  |
|   23 | Telnet               |
|   25 | SMTP                 |
|   53 | DNS                  |
|   80 | HTTP                 |
|  110 | POP3                 |
|  143 | IMAP                 |
|  443 | HTTPS                |
| 3306 | MySQL                |
| 3389 | Remote Desktop (RDP) |

## How It Works

1. The user enters a hostname or IP address.
2. The program resolves the hostname to an IP address.
3. It attempts to connect to a list of common TCP ports.
4. If a connection is successful, the port is marked as **OPEN**.
5. When possible, the program retrieves the service banner.
6. A scan report is displayed after the scan is complete.

## How to Run

### Prerequisites

* Python 3.x installed on your system

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Python-Network-Socket-Port-Scanner.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Python-Network-Socket-Port-Scanner
   ```

3. Run the program:

   ```bash
   python port_scanner.py
   ```

4. Enter the target hostname or IP address when prompted.

## Example

### Input

```text
Enter Hostname or IP Address: scanme.nmap.org
```

### Output

```text
Scanning 45.33.32.156
------------------------------
Port 22 (SSH) is OPEN
Service Banner: SSH-2.0-OpenSSH

Port 80 (HTTP) is OPEN
Service Banner: HTTP/1.1 200 OK

Scan Completed.
```

## Applications

* Learn basic network programming
* Understand TCP socket communication
* Identify open ports on a target host
* Explore common network services
* Educational cybersecurity and networking practice

## Limitations

* Scans only a predefined list of common TCP ports
* Banner detection depends on whether the target service provides one
* Does not scan UDP ports
* Intended for educational and authorized use only

## Future Improvements

* Scan custom port ranges
* Support scanning multiple IP addresses
* Use multithreading for faster scans
* Export scan results to a text or CSV file
* Add service detection using protocol-specific requests
* Build a graphical user interface (GUI)

## Disclaimer

This tool is intended **only for educational purposes and authorized security testing**. Always obtain permission before scanning any network or system that you do not own or administer.

## Learning Outcomes

This project demonstrates:

* Python socket programming
* TCP client connections
* Port scanning techniques
* Hostname resolution
* Exception handling
* Basic service banner detection
* Network security fundamentals

## Author

**Yug Gandhi**

Internship Task 2 – Python Network Socket Port Scanner
