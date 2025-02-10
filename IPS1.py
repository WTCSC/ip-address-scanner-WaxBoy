#!/usr/bin/env python3
import ipaddress
import re
import subprocess
import argparse

def scan_network(cidr, timeout, ports):
    '''
    Scans a given network (CIDR notation) by pinging each host and, if responsive, running an Nmap scan on the specified ports.
    
    Parameters:
      cidr (str): Network in CIDR notation (eg., '192.168.1.0/24').
      timeout (int): Ping timeout in ms (eg., 10, 500)
      ports (str): Port(s) to scan. Can be a single port, a comma(only)-separated list, or a range (eg., '22', '80,443', '1-100').
    '''
    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError as e:
        print(f"ERROR: Invalid network '{cidr}': {e}")
        return

    UP = 0
    DOWN = 0

    # Print a header for the output table
    print('=' * 80)
    print("IP Address       Status   Ping Time (ms)  Nmap Open Ports")
    print("=" * 80)

    for ip in network.hosts():
     
        # Attempt to ping
        # Note: The parameters below work for Unix systems.
        PING = subprocess.run(['ping', str(ip), '-c', '1', '-W', str(timeout)], capture_output=True, text=True)
        PING_OUT = PING.stdout

        if '0 received' not in PING_OUT:

            # Try to extract the ping time
            match = re.search(r'time=([\d\.]+)', PING_OUT)
            PING_TIME = match.group(1) if match else "N/A"

            # Run Nmap on the IP for the specified ports
            
            NMAP = subprocess.run(['nmap', '-p', ports, str(ip)], capture_output=True, text=True)
            # Look for lines containing 'open'
            open_ports = []
            for line in NMAP.stdout.splitlines():
                if re.search(r'\bopen\b', line):
                    open_ports.append(line.strip())
            nmap_summary = f"\n {' ' * 41}".join(open_ports) if open_ports else "No open ports"


        # Initially used 16 - len(str(ip)), replaced with :<16 for simplicity
            print(f"{str(ip):<16} {'UP':<8} {PING_TIME:<15} {nmap_summary}")
            UP += 1
        else:
            print(f"{str(ip):<16} {'DOWN':<8} {'N/A':<15} No response in {timeout * 1000} ms")
            DOWN += 1

    # Final Stats
    print("=" * 80)
    print(f"Scan complete: \n{' ' * 16}UP: {UP}   DOWN: {DOWN}\n{' ' * (31 + len(str(UP)) + len(str(DOWN)))}Total scanned: {UP + DOWN}")

def main():
    
    #ARGPARSE
    parser = argparse.ArgumentParser(description="Simple Network Scanner")
    parser.add_argument("input", help="IP address in CIDR notation: 'xxx.xxx.xxx.xxx/XX'")
    parser.add_argument("-t", "--timeout", type=int, default=20, help="Timeout in ms before marking an IP as DOWN (default: 20 ms).")
    parser.add_argument("-p", "--port", type=str, required=True, help="Port(s) to scan (eg., '22', '80,443', or '1-100').")
    args = parser.parse_args()

    # Convert ms to seconds for the ping command.
    timeout_seconds = args.timeout / 1000.0
    scan_network(args.input, timeout_seconds, args.port)

if __name__ == "__main__":
    main()
