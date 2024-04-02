import psutil
import socket
import time


# Function to get network information
def get_network_info():
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                ip_address = address.address
                return interface_name, ip_address
    return None, None

# Function to open get uptime
def get_uptime():
        uptime = psutil.boot_time()
        return str(round((time.time() - uptime) / 3600, 1)) + " hours"

def get_network_info():
    ifaces = psutil.net_if_addrs()
    for iface in ifaces:
        if iface == 'Ethernet':
            return ifaces[iface][0].address
        elif iface == 'Wi-Fi':
            return ifaces[iface][0].address
    return "Not Connected"