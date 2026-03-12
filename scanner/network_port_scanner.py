import socket
import os
from concurrent.futures import ThreadPoolExecutor


def is_host_alive(ip):
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    return response == 0


def scan_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))

        if result == 0:
            return f"Port {port}: Open"
        else:
            return f"Port {port}: Closed"


def scan_ports(ip, port_range):
    print(f"\nScanning ports for {ip}...")

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in port_range]

        for future in futures:
            print(future.result())


def main():
    subnet = input("Enter subnet (e.g., 192.168.1.): ")
    port_start = int(input("Enter start port: "))
    port_end = int(input("Enter end port: "))

    for i in range(1, 255):
        ip = f"{subnet}{i}"

        print(f"\nPinging {ip}...")

        if is_host_alive(ip):
            print(f"{ip} is alive")
            scan_ports(ip, range(port_start, port_end + 1))
        else:
            print(f"{ip} is not responding")


if __name__ == "__main__":
    main()
