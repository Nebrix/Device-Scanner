import customtkinter
from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
from maintenance.update import update
import netifaces

def get_vendor_name_from_mac(mac_address):
    try:
        vendor_name = MacLookup().lookup(mac_address)
        return vendor_name
    except Exception as e:
        return "Error: " + str(e)

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

    output_text.delete(1.0, "end")
    for device in devices:
        vendor_name = get_vendor_name_from_mac(device['mac'])
        output_text.insert("end", f"IP: {device['ip']}, MAC: {device['mac']}, Vendor: {vendor_name}\n")

def on_scan_button_click():
    scan_network()

def on_update_button_click():
    update()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x500")

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(fill='both', expand=True)

scan_frame = tabview.add("Scan")

scan_button = customtkinter.CTkButton(scan_frame, text="Scan Network", command=on_scan_button_click)
scan_button.pack(padx=20, pady=20)

output_text = customtkinter.CTkTextbox(scan_frame, height=2000, width=2000)
output_text.pack(padx=20, pady=20)

update_frame = tabview.add("Update")

update_button = customtkinter.CTkButton(update_frame, text="Update", command=on_update_button_click)
update_button.pack(padx=20, pady=20)

app.mainloop()