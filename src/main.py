from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from maintenance.update import update
import netifaces
import sys
import os

def get_vendor_name_from_mac(mac_address):
    try:
        vendor_name = MacLookup().lookup(mac_address)
        return vendor_name
    except Exception as e:
        print("Error:", e)
        return None

def get_default_gateway():
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    return default_gateway

def scan_network():
    gateway = get_default_gateway()
    arp = ARP(pdst=str(gateway) + '/24')
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, recv in result:
        devices.append({'ip': recv.psrc, 'mac': recv.hwsrc})

    for device in devices:
        vendor_name = get_vendor_name_from_mac(device['mac'])
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {vendor_name}")


def main():
    if os.name == "nt" and sys.argv[1] == "/!":
        update()
    elif os.name != "nt" and sys.argv[1] == "--update":
        update()
    else:
        scan_network()

if __name__ == '__main__':
    main()