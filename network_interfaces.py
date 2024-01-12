import psutil
addrs = psutil.net_if_addrs()

interface_addresses = []

def get_interfaces():
    for interface, addresses in addrs.items():
        print(f"Network Interface: {interface}")
        interface_addresses.append([interface, addresses[1].address])
    return interface_addresses

print(interface_addresses)