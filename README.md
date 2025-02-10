[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17928376)

# IP Scanner

This script is designed to allow you to scan and ping each of the connections on a given subnet, relaying if they are responsive (UP), or unresponsive (DOWN).

## How does it work?

* The script takes an IP, given in CIDR notation (eg., `192.168.0.1/24`)
* It looks over every valid host IP on the network and sends a PING request and scans (optional) ports on each of those IPs.
* If given a response, it will return with **UP**, the response time, and the status of the requested ports.
* If no response given in the allotted TIMEOUT time, it will return with **DOWN**
* Lastly, it displays the total connections that are **UP** & **DOWN** 

## Usage

### Prerequisites:

* Python Version 3.7+
* Unix-based system (Linux or macOS)

### Running:

1. Open the command line and navigate to the directory that contains the script `IPS1.py`

2. Run using this command:
    ``` 
    python3 IPS1.py "IP/SUBNET" [-t "TIMEOUT(ms)"] [-p "PORT(s)"]
    ```
    * **IP** is the ip address you want to test. (eg., `192.168.0.1`)
    * **/SUBNET** represents the CIDR notation for a subnet mask (eg., `/24`)
    * *Optionally,* **TIMEOUT** can be a number of ms from 1-999 to wait for a PING response (default is 20 ms)
    * *Optionally,* **PORT(s)** can be a single port, a list separated by commas, or a range (eg., '80', '22,443,5000', '1-100')

### Example:


    python3 IPS1.py 10.0.2.1/29 -t 10 -p 80,433
    

### Output 

```
================================================================================
IP Address       Status   Ping Time (ms)  Nmap Open Ports
================================================================================
10.0.2.1         DOWN     N/A             No response in 10.0 ms
10.0.2.2         UP       0.306           80/tcp  open  http
                                          443/tcp open  https
10.0.2.3         UP       0.283           80/tcp  open  http
                                          443/tcp open  https
10.0.2.4         UP       0.325           80/tcp  open  http
                                          443/tcp open  https
10.0.2.5         DOWN     N/A             No response in 10.0 ms
10.0.2.6         DOWN     N/A             No response in 10.0 ms
================================================================================
Scan complete: 
                UP: 3   DOWN: 3
                                 Total scanned: 6
 ```

## Notes

* The script is designed to wait for a response or a timeout before continuing, meaning larger loads might take a long time.

* Adjust TIMEOUT to be lower for faster results. (eg., 5 or 10 ms on a local network) 

* Adjust TIMEOUT to be higher to ensure no slow networks are being marked as DOWN.

* Ports separated by a comma AND a space will **NOT** work (eg. '80, 433, 169')