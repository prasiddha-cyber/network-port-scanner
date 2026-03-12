# Network Port Scanner

## Overview
This project is a Python-based network scanning tool that detects live hosts in a subnet and scans ports to identify open and closed services.

## Features
- Detects live hosts using ping
- Scans ports within a specified range
- Identifies open and closed ports
- Multi-threaded scanning for faster performance

## Technologies Used
- Python
- Socket Programming
- ThreadPoolExecutor

## Project Structure

scanner/
- network_port_scanner.py

requirements.txt
- Python dependencies (if required)
  
README.md
- Project documentation

## How It Works
1. The user enters a subnet (example: 192.168.1.)
2. The program pings each IP address in the subnet to identify active hosts
3. For each live host, the scanner checks a range of ports
4. The tool prints whether each port is open or closed

## Example Usage

Run the program:

python scanner/network_port_scanner.py

Input example:

Enter subnet: 192.168.1.  
Enter start port: 20  
Enter end port: 80

## Purpose
This project demonstrates basic network reconnaissance techniques used in cybersecurity and penetration testing.

## Author
Pingali Prasiddha  
Cyber Security Student
