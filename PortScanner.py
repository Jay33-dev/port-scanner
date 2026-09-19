import socket
import time

# list of ports for testing.
ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 443, 3000]

# function to check if port is open.
def port_scan(target_ip, port):
    # returns True, it's open.
    try:
        with socket.create_connection((target_ip, port), timeout=1):
            return True
    # returns false, closed or filtered.
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

# While loop checking if IP or domain name is valid.
while True:
    # asking user for IP or hstname.
    target = input("Please enter a domain or an IP address: ")

    # getting IP with domain name and checks if IP or domain name is valid at the same time.
    try:
        target_ip = socket.gethostbyname(target)

        # telling the user it's starting the scan.
        print(f"Starting scan on {target} ({target_ip})")
        # storing the starting time.
        start = time.time()

        # testing every ports in the list using IP entered by user.
        for port in ports:
            # checks if port is open using the port_scan function.
            if port_scan(target_ip, port):
                # telling it's open.
                print(f"Port {port} is open")
            else:
                # telling port is closed or filtered.
                print(f"Port {port} is closed or filtered")

        # storing end time.
        end = time.time()
        # telling how much time it took.
        print(f"Time taken: {end - start:.2f} seconds")

        # while loop checking if user wants to continue and for bad user input.
        while True:
            # asking for choice and handles upper case too.
            choice = input("Do you wich to continue? (y or n): ").lower()
            # if choice is valid break while loop.
            if choice in ("y", "n"):
                break
            # else asks for a valid answer.
            print("Please enter y or n.")

        # if choice is yes continue.
        if choice == "y":
            continue
        # else break while loop and end program.
        else:
            break

    # checks for error in IP or domain name given by user.
    except socket.gaierror:
        # telling user IP or domain is not valid.
        print("Domain or IP address not valid.")
