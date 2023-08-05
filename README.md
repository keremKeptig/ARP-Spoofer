# ARP-Spoofer
This code is a Python script that performs an ARP spoofing attack. ARP spoofing is a type of network attack that allows devices on a local network to intercept and even manipulate communications between other devices in the network.

 Here is a script that can be used to monitor the internet traffic between a device and the local network gateway. 

## These steps will guide you on how to run the code:

- Install Python and required libraries: You must install the scapy and getmac libraries. You can install the necessary libraries using the following commands in the terminal:
  
1. ` pip install scapy `

2. `pip install argparse `

3. `pip install getmac
`
- **Syntax:** python **file_name** -t **[target IP]** -g **[router IP]**
  
1. `[target IP]` should be the IP address of the target machine.

2. `[router IP]` should be the IP address of the gateway (router).

*E.g.* `python arp_spoof.py -t 192.168.1.100 -g 192.168.1.1
`
- **REMINDER:** Use with root/administrative privileges.
#
To move forward, you need to have argparse, ipaddress, and scapy installed.

You can install the necessary libraries using the following commands in the terminal:

* pip install argparse
 
* pip install scapy
  
* pip install getmac


 ##  Legal Disclaimer:
Use only for tests on your own network and do not carry out such attacks against illegal or unauthorized networks. Performing such an attack without knowledge of network security and ethical issues can have serious consequences. It is the end user's responsibility to comply with all applicable local, state and federal laws.
