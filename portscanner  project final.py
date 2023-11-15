import socket  #Socket library connects with network

def scan_ports(target, start_port, end_port):   #Defining a port scan function 
    print(f"Scanning target {target} for open ports...\n") #Print open port results
    
    for port in range(start_port, end_port + 1): #looping in port rage
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#This line creates a TCP socket (SOCK_STREAM) using the IPv4 address family (AF_INET).
        sock.settimeout(1) #This line sets a timeout of 1 second for the socket connection attempt.
        result = sock.connect_ex((target, port)) #The connect_ex method returns 0 if the connection is successful
        if result == 0: #If the result is 0, it means the port is open
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter start port: ")) # It takes user input for the target IP address and port range and then calls the scan_ports function with the provided parameters.
    end_port = int(input("Enter end port: "))

    scan_ports(target_ip, start_port, end_port)
