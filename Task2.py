import socket

common_ports = {
    20: "FTP (Data)",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "Remote Desktop"
}

host = input("Enter Hostname or IP Address: ")

try:
    host = socket.gethostbyname(host)
except socket.gaierror:
    print("Invalid Hostname or IP Address.")
    exit()

print("\nScanning", host)
print("-" * 30)

for port, service in common_ports.items():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} ({service}) is OPEN")

        try:
            if port == 80:
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")

            banner = s.recv(1024).decode(errors="ignore").strip()

            if banner:
                print("Service Banner:", banner)
            else:
                print("Service Banner: Not Available")

        except:
            print("Service Banner: Not Available")

    s.close()

print("\nScan Completed.")