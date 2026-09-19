import socket
import time

"""Ports for testing"""
ports = [1,2,3,4,5]

"""Creation of socket"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""asking for hostname"""
target = input("Please enter a host: ")
"""getting IP from hostname"""
target_ip = socket.gethostbyname(target)

"""telling the user the scan is starting"""
print(f"Starting scan on {target} ({target_ip})")

"""function trying to connect to IP using a specif port"""
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

"""Starting time"""
start = time.time()

"""Using ports in the list"""
for port in ports:
    if port_scan(port):
        """telling user if port is open"""
        print(f"port {port} is open")
    else:
        """telling user if port is closed"""
        print(f"port {port} is closed")

"""end time"""
end = time.time()
"""Telling the user how much time it took to scan ports in list"""
print(f"Time taken {end - start:.2f} seconds")