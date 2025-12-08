import socket #Creates network connection

ERROR_CODES = {  #Creates a dictionary called ERROR_CODES
    0: "OPEN",  #Open means the port is open
    10035: "CLOSED"
}
def get_error_description(code): 
    """Return description for a socket error code."""
    return ERROR_CODES.get(code, "CLOSED - Unknown error")    #Looks up the code inside the ERROR_CODES dictionary. If its not in the dictionary, it returns "CLOSED"- unknown error

def scan_port(ip, port): 
    """
    Scan a single port and return the connect_ex result. #Scans every single port then returns 0 if open, non-zero if closed or error.
    0= open port
    non-zero = closed/error
    """
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creates a TCP socket
    s.settimeout(1) # 1 second timeout  #Sets 1-second timeout. If the connection takes longer than 1 second, it will error out instead of hanging forever.
    result = s.connect_ex((ip, port))   #Connects to target ip and port
    description = get_error_description(result) #Converts the numeric recult code into a human-readable message

    print(f"Port {port}: {result} ({description})") #Prints a line of the scanned ports with its description

    s.close()  #Closes to free resources
    return result  #Returns the numeric result code to the caller so other functions can decide if the port is open

def scan_selected_ports(ip, ports):  #Defines scan_selected_ports with target ip and ports
    """Scan specific list of ports (e.g., 21, 22, 80, 443)."""
    print(f"\nScanning selected ports on {ip}: {ports}\n")
    
    open_ports = []  #Creates an empty list to store ports that are found open
    
    for port in ports: #Loops through each port in the port list
        try:  #Try block just in case something goes wrong
            result = scan_port(ip, port)
            if result == 0: #open port  #checks if the result is 0 meaning port is open
                open_ports.append(port) #if open, adds that port number to the open_port list
        except Exception as e:
            print (f"Error scanning port {port}: {e}")   #If anything goes wrong such as network error, it catches the exception and prints an error instead of crashing
    print("\nOpen selected ports:", open_ports)   #After finishing the loop, prints all open ports in the selected list

def scan_range(ip, start_port, end_port): #Defines a function that scans a range 
    """Scan a continuous range of ports."""
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    
    open_ports = []
    
    for port in range (start_port, end_port + 1):   #Loops start_port up to and including end_port 
        try:
            result = scan_port(ip, port)
            if result == 0: #open port
                open_ports.append(port)

        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    print("\nOpen ports found:", open_ports)


if __name__ == "__main__":
    target_ip = "192.168.1.101" #Set the IP that you want to scan
    common_ports = [21, 22, 80, 443] #Port numbers that you want to scan
    scan_selected_ports(target_ip, common_ports)


