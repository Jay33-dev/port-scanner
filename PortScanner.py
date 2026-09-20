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

def ip_from_domain(domain):
    return socket.gethostbyname(domain)

def stop_or_continue():
    # while loop checking if user wants to continue and for bad user input.
    while True:
        # asking for choice and handles upper case too.
        choice = input("Do you wish to continue? (y or n): ").lower()

        # if choice is valid break while loop.
        if choice in ("y", "n"):
            # if choice is yes continue.
            if choice == "y":
                return True
            # else break while loop and end program.
            else:
                return False
        else:
            # else asks for a valid answer.
            print("Please enter y or n.")

while True:
    # asking the user to make a choice
    choice = input(
        "1. Scan a subnet.\n"
        "2. Scan a specific IP address or domain.\n"
        "3. Get a IP address from a domain.\n"
        "4. Exit\n"
        "Enter a number: "
    )

    if choice == "1":
        # subnet scanning has not been implemented yet.
        pass

    elif choice == "2":
        # While loop checking if IP or domain name is valid.
        while True:
            # asking user for IP or hostname.
            target = input("Please enter a domain or an IP address: ")

            # getting IP with domain name and checks if IP or domain name is valid at the same time.
            try:
                target_ip = ip_from_domain(target)

                # telling the user it's starting the scan.
                print(f"Starting scan on {target} ({target_ip})")

                # storing the starting time.
                start = time.time()

                # testing every port in the list using IP entered by user.
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

                # asking the user if they want to continue.
                should_continue = stop_or_continue()

                # if user chooses yes, continue asking for an IP or domain.
                if should_continue:
                    continue
                # else break while loop and return to the main menu.
                else:
                    break

            # checks for error in IP or domain name given by user.
            except socket.gaierror:
                # telling user IP or domain is not valid.
                print("Domain or IP address not valid.")

    elif choice == "3":
        while True:
            target = input("Please enter a domain: ")

            try:
                target_ip = ip_from_domain(target)
                print(f"The IP address for {target} is {target_ip}")

                # asking the user if they want to continue.
                should_continue = stop_or_continue()

                # if user chooses yes, continue asking for an IP or domain.
                if should_continue:
                    continue
                # else break while loop and return to the main menu.
                else:
                    break

            except socket.gaierror:
                print("Please enter a valid domain...")

    elif choice == "4":
        break

    else:
        print("Choice is not valid...")