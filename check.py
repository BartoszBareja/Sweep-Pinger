import psutil
addrs = psutil.net_if_addrs()

for interface, addresses in addrs.items():
    print(f"Network Interface: {interface}")
    for address in addresses:
        print(f"  Address: {address.address}\n")