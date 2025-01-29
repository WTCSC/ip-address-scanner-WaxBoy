import sys
import ipaddress
import os
import re
import subprocess


def function():
    TIMEOUT = .02 #default timeout of 20ms
    
    #make sure input is used correctly
    if len(sys.argv) != 2:   
                        #if theres a 3rd argument it must be a number amount from 1-999 to use as ms timeout
        if re.search(r'[\d]{1,3}', sys.argv[2]) and len(sys.argv) == 3 and sys.argv[2] != 0:
        
            TIMEOUT = int(sys.argv[2])/1000   #converts ms into s
        
        else:                                                                   #takes just the filename not the whole path
            print(f"ERROR: Input should look as follows: \n\n    ``` \n        python3 {os.path.basename(__file__)} 'ip' \n                            ```")
            return 1

    #takes input
    INPUT = sys.argv[1]
                        #Ensures proper ip format 0.0.0.0/0 - 999.999.999.999/99  (assumes it will not work if an invalid IP)
    if not re.search(r"^(\d{1,3}[.]){3}\d{1,3}[/]\d{1,2}$", INPUT):

        print(f"ERROR: Invalid IP format. Correct format: \n\n``` \n '255'.'255'.'255'.'255'/'32' \n                                     ```")
        return 2

    #grabs a bunch of information on the IP's network
    network = ipaddress.ip_network(INPUT, strict=False)

    #Initialize count
    UP = 0
    DOWN = 0

    #Iterate over the valid host ips from the network
    for ip in network.hosts():                          
                                #only send 1 packet and only wait ms for a response   #captures output as byte string and turns it into text
        PING = subprocess.run(['ping', f'{ip}', '-c', '1', '-W', str(TIMEOUT)], text=True, capture_output=True) 
        
            #if theres no response the ping's output will contain '0 received'
        if '0 received' not in PING.stdout:
                        #make sure the results are always in-line       #grab the time from the output.
            print(f"{ip}{(' ') * (16 - len(str(ip)))}-  UP  ({re.search(r'time=([\d]+[.][\d]{3})', PING.stdout).group(1)} ms)\n")
        
        else:                                         #explain that DOWN does not ensure the network is down because it might have a long response time-- to be tested using higher TIMEOUTs
            print(f"{ip}{(' ') * (16 - len(str(ip)))}- DOWN (No response in {int(TIMEOUT * 1000)} ms)")

        #count     
        if PING.returncode == 0:
            UP += 1
        else:
            DOWN += 1
        
        
            #STATS
    print(f"\n Scan complete \n\n UP : {UP} \n\n DOWN : {DOWN} \n\n Total Scanned : {UP + DOWN}")


function()

