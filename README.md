[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17928376)

# IP Scanner

This script is designed to allow you to scan and ping each of the connections on a given subnet, relaying if they are responsive (UP), or unresponsive (DOWN).

## How does it work?

* The script takes an IP, given in CIDR notation (eg., `192.168.0.1/24`)
* It looks over every valid host IP on the network and sends a PING request
* If given a reponse, it will return with **UP** and the response time
* If no response given in the alotted TIMEOUT time, it will return with **DOWN**
* Lastly, it displays the total connections that are **UP** & **DOWN** 

## Usage

### Prerequesites:

* Python Version 3.7+
* Unix-based system (Linux or mac-os)

### Running:

1. Open the command line and nagivate to the directory that contains the script `IPS.py`

2. Run using this command:
    ``` 
    python3 IPS.py "IP/SUBNET" [TIMEOUT(ms)]
    ```
    * **IP** is the ip address you want to test. (eg., `192.168.0.1`)
    * **/SUBNET** represents the CIDR notation for a subnet mask (eg., `/24`)
    * *Optionally,* **TIMEOUT** can be a number of ms from 1-999 to wait for a PING response (default is 20 ms)

### Example:


    python3 IPS.py 10.0.2.1/29 50
    

### Output 

```
10.0.2.1        - DOWN (No response in 50 ms)
10.0.2.2        -  UP  (0.320 ms)

10.0.2.3        -  UP  (0.262 ms)

10.0.2.4        -  UP  (0.169 ms)

10.0.2.5        - DOWN (No response in 50 ms)
10.0.2.6        - DOWN (No response in 50 ms)

 Scan complete 

 UP : 3 

 DOWN : 3 

 Total Scanned : 6
 ```

## Notes

* The script is designed to wait for a response or a timeout before continuing, meaning larger loads might take a long time.

* Adjust TIMEOUT to be lower for faster results. (eg., 5 or 10 ms on a local network) 

* Adjust TIMEOUT to be higher to ensure no slow networks are being marked as DOWN.