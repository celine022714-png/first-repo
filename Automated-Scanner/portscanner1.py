import socket #Imports the socket library so we can create TCP connections

ERROR_CODES = {  #A list of dictionary called Error codes
    0: "OPEN",  #A 0 indicates the connection is open. 
    10035: "CLOSED",  #The number indicates the connection is closed.
}   #closes the dictionary
def get_error_description(code):  #Defines a helper function that takes an error code.
    """Return description for a socket error code."""
    return ERROR_CODES.get(code, "CLOSED - Unknown error")  #Looks up the code in ERROR_CODES. If its not there, returns "CLOSED" or "unknown error" as default.
def scan_port(ip, port):   #Defines a function that checks a specific port on an IP address
    """
    Scan a single port and return the connect_ex result.
    0= open port
    non-zero = closed/error
    """

    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creates a TCP socket
    s.settimeout(1) # 1 second timeout #Sets a 1 second timeout so it doesnt hang forever on a dead port

    result = s.connect_ex((ip, port)) # 0 = success (open port) #Tries to connect to ip and port. Returns 0 if the connection succeeds. Return a non-zero error code if it fails.
    description = get_error_description(result) #Translates that result error code into a text description using the helper func.

    print(f"Port {port}: {result} ({description})")  #Prints the port number, the numeric code, and the description

    s.close()  #Closes the socket to free resources
    return result

def scan_range(ip,start_port, end_port): #Defines a function to scan many ports in a range on the given IP
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n") #Prints a header showing what IP and port range you are scanning
    open_ports = [] #Creates an empty list to store any ports that are found open

    for port in range(start_port, end_port + 1): #Lopps through every port from start up to end port
        try: #Try block to safely handle any errors while scanning
            result = scan_port(ip, port)
            if result == 0: #open port #Checks if the return code is 0, means the port is open
                open_ports.append(port) #If its open, adds the port number to the open_port list

        except Exception as e:
            print(f"Error scanning port {port}: {e}") #Print an error message telling you which port failed and why
    print("\nOpen ports found:", open_ports) #Prints a summary list of all open ports that were found


if __name__ == "__main__": 
    target_ip = "192.168.1.101"  #Sets the IP address you want to scan
    start = 20 #First port in the scanning range
    end = 80 #Last port in the scanning range

    scan_range(target_ip, start, end)
