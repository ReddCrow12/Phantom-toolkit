import socket
import threading
from colorama import Fore, init
import datetime   
import requests   
from colorama import Fore, init
import getpass
import os
import subprocess

start_time = datetime.datetime.now()
init()

def scan_port(ip, port):
  try:
    sock = socket.socket()
    sock.connect((ip, port))
    print("  [+] Port Opened " + str(port))
  except:
      pass
  
def scan(target, ports):
   print('\n' + 'Starting Scan For '+ str(targets)) 
   for port in range(1,ports):
      scan_port(target, port)

def list_connections():
    print(f"{Fore.YELLOW}Listing active connections...{Fore.RESET}")
    nets_command = f"netstat -tn"
    result = os.system(nets_command)
    return result

def disconnect(ip, port):
    print(f"Attempting to disconnect {ip}:{port}...")
    cmd = f'netstat -ano | findstr {ip}:{port}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        lines = result.stdout.strip().split('\n')
        for line in lines:
            parts = line.split()
            if len(parts) == 5:
                pid = parts[-1]
                print(f"Found connection to {ip}:{port} with PID: {pid}")
                kill_cmd = f'taskkill /PID {pid} /F'
                kill_result = subprocess.run(kill_cmd, shell=True, capture_output=True, text=True)
                if kill_result.returncode == 0:
                    print(f"{Fore.GREEN}Successfully disconnected {ip}:{port}{Fore.RESET}")
                else:
                    print(f"{Fore.RED}Error disconnecting {ip}:{port}: {kill_result.stderr.strip()}{Fore.RESET}")
            else:
                print(f"{Fore.RED}Unexpected netstat output format: {line}{Fore.RESET}")
    else:
        print(f"{Fore.RED}No active connection found for {ip}:{port}{Fore.RESET}")

print(f"{Fore.LIGHTMAGENTA_EX}<-Date/Time->: {Fore.RESET}", start_time)

print(f'''{Fore.LIGHTWHITE_EX}

 ▄▀▀▄ ▄▀▄  ▄▀▀▄▀▀▀▄      ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄ 
█  █ ▀  █ █   █   █     █   █   █ █  █   ▄▀ ▐ ▄▀ ▀▄ █  █ █ █ █    █  ▐ █      █ █  █ ▀  █ 
▐  █    █ ▐  █▀▀█▀      ▐  █▀▀▀▀  ▐  █▄▄▄█    █▄▄▄█ ▐  █  ▀█ ▐   █     █      █ ▐  █    █ 
  █    █   ▄▀    █         █         █   █   ▄▀   █   █   █     █      ▀▄    ▄▀   █    █  
▄▀   ▄▀   █     █        ▄▀         ▄▀  ▄▀  █   ▄▀  ▄▀   █    ▄▀         ▀▀▀▀   ▄▀   ▄▀   
█    █    ▐     ▐       █          █   █    ▐   ▐   █    ▐   █                  █    █    
▐    ▐                  ▐          ▐   ▐            ▐        ▐                  ▐    ▐    

{Fore.RESET}''')

while True:
    key = input(f"{Fore.LIGHTMAGENTA_EX}Phantom>:{Fore.RESET} ")

    if key == 'info':
        print(''' ''')
        print(f"{Fore.LIGHTGREEN_EX} +--------------------- MANU INFO ---------------------+ {Fore.RESET}")
        print(f''' [+] The menu is the most important place in this tool.
     You have a lot of commands that you can type in order to get
     the full power of the {Fore.LIGHTMAGENTA_EX}Phantom tool.{Fore.RESET}
     To get more information about the tool and commands, type 'help'.''')
        print(''' ''')

    elif key == 'help':
        print(f'''{Fore.LIGHTWHITE_EX}

     ██░ ██ ▓█████  ██▓     ██▓███  
    ▓██░ ██▒▓█   ▀ ▓██▒    ▓██░  ██▒
    ▒██▀▀██░▒███   ▒██░    ▓██░ ██▓▒
    ░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██▄█▓▒ ▒
    ░▓█▒░██▓░▒████▒░██████▒▒██▒ ░  ░
     ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░▒▓▒░ ░  ░
     ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░▒ ░     
     ░  ░░ ░   ░     ░ ░   ░░       
     ░  ░  ░   ░  ░    ░  ░         

        {Fore.RESET}''')
        print(f"""
    {Fore.LIGHTMAGENTA_EX}Phantom Hacking Tool - Help Section
    ===================================={Fore.RESET}

    Welcome to Phantom, a powerful hacking tool designed for ethical hacking and cybersecurity enthusiasts.
    Below you will find detailed information about the various features and commands available in Phantom.

    Commands:
    ---------
    1. help  - Display this help information.
    2. -a    - Run the automated attack module.
    3. info  - Display information about Phantom and its capabilities.
    4. connect <PORT> <IP> - Connect to a target using the specified port and IP address.
        - Supports SSH and Telnet connections on ports 22 and 23 respectively.
    5. scantom <TARGET> - Scan the specified target(s) for open ports.
        - Example: scantom 192.168.1.1
    6. connlist - List all active TCP connections.
        - Displays the local address, remote address, and the state of each connection.
    7. disconnect <IP> <PORT> - Disconnect a connection to the specified IP and port.
        - Example: disconnect 192.168.1.1 80
    8. exit - Exit the tool and return to the terminal/cmd.

    {Fore.LIGHTMAGENTA_EX}Phantom Capabilities:
    ---------------------{Fore.RESET}
    1. Network Scanning:
       Phantom can perform extensive network scans to identify active devices, open ports, and potential vulnerabilities.

    2. Exploitation:
       Use Phantom to exploit known vulnerabilities in systems and applications, gaining unauthorized access to test security measures.

    3. Connection Management:
       List and manage active connections, including the ability to disconnect specific connections.

    4. Reporting:
       Generate comprehensive reports of your penetration tests, including identified vulnerabilities, exploitation steps, and remediation suggestions.

    {Fore.LIGHTMAGENTA_EX}Usage Examples:
    ---------------{Fore.RESET}
    - To run an automated attack:
      $ Phantom>: -a [type of attack] [IP]

    - To connect to a target:
      $ Phantom>: connect <PORT> <IP>

    - To scan a network:
      $ Phantom>: scantom <TARGET>

    - To list active connections:
      $ Phantom>: connlist

    - To disconnect a connection:
      $ Phantom>: disconnect <IP> <PORT>

    - To display tool information:
      $ Phantom>: <tool name> info

    {Fore.LIGHTMAGENTA_EX} Important Notes:
    ----------------{Fore.RESET}
    - Phantom is intended for use in authorized security testing and research only.
    - Unauthorized use of this tool is illegal and unethical.
    - Always obtain proper permissions before conducting any tests.
""")
    elif key == 'connect info':
        print(''' ''')
        print(f"{Fore.LIGHTGREEN_EX} +---------------- CONNECT INFO ----------------+ {Fore.RESET}")
        print(f''' [+] The 'connect' command allows you to establish connections using various protocols.
  You can connect using SSH, Telnet, or via Bind Shell.
  Syntax:
  - For SSH: 'connect [ssh port] [IP]'
  - For Telnet: 'connect [telnet port] [IP]'
  - For Bind Shell: 'connect [bind shell port] [IP]'
  Remember to replace [IP] and [port] with the appropriate values.
  To exit the connection, use the 'exit' command.''')
        print(''' ''')
    elif key == 'scantom info':
        print(f"{Fore.LIGHTGREEN_EX} +--------------------- SCANTOM INFO ---------------------+ {Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}The 'scantom' command allows you to scan for open ports on one or more target IP addresses.{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}Usage: scantom <TARGET>{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}TARGET can be a single IP address or a comma-separated list of IP addresses.{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}You will be prompted to enter the number of ports to scan (starting from port 1).{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}Example: scantom 192.168.1.1 or scantom 192.168.1.1,192.168.1.2{Fore.RESET}")
    elif key == 'connlist info':
        print(f"{Fore.LIGHTGREEN_EX} +--------------------- CONNLIST INFO ---------------------+ {Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}The 'connlist' command lists all active TCP connections.{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}It displays the local address, remote address, and the state of each connection.{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}Example: connlist{Fore.RESET}")
    elif key == 'connlist':
        list_connections()
    elif key.startswith('disconnect'):
        try:
            _, ip, port = key.split()
            port = int(port)
            disconnect(ip, port)
        except ValueError:
            print(f"{Fore.RED}Invalid command format. Use: disconnect <IP><PORT>{Fore.RESET}")
    elif key.startswith('scantom'):
        
            _, targets = key.split()
            ports = int(input(f"{Fore.LIGHTMAGENTA_EX}[*] Enter How Many Ports You want to Scan: {Fore.RESET}"))
        
            if ',' in targets:
                print("[*] Scanning Multiple Targets")
                for ip_addr in targets.split(','):
                    scan(ip_addr.strip(' '), ports)
            else:
                scan(targets, ports)
    
    elif key.startswith('connect'):
        try:
            _, port, ip = key.split()
            port = int(port)
            buffer_size = 2048

            if port == 22:
                username = input("Enter the SSH username: ")
                print(f"{Fore.GREEN}Attempting to connect to {ip} on port {port} using SSH{Fore.RESET}")
                
                ssh_command = f"ssh {username}@{ip} -p {port}"
                os.system(ssh_command)
                
            elif port == 80:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((ip, port))
                    print(f"{Fore.GREEN}Successfully connected to {ip} on port {port} (HTTP){Fore.RESET}")
                    
                    request = f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
                    s.send(request.encode())
                    response = s.recv(buffer_size).decode()
                    print(response)
                    
                except socket.error as e:
                    print(f"{Fore.RED}HTTP Connection error: {e}{Fore.RESET}")
                finally:
                    s.close()
                
            elif port == 23:
                try:
                  print(f"{Fore.GREEN}Attempting to connect to {ip} on port {port} using Telnet{Fore.RESET}")
                  os.system(f"telnet {ip} {port}")

                except socket.error as e:
                    print(f"{Fore.RED}Telnet Connection error: {e}{Fore.RESET}")
                    
            else:
                
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect((ip, port))
                    print(f"{Fore.GREEN}Successfully connected to {ip} on port {port}{Fore.RESET}")

                    while True:
                        command = input("Enter the command for shell: ")
                        s.send(command.encode())

                        if command.lower() == 'exit':
                            break

                        results = s.recv(buffer_size).decode()
                        print(results)
                        
                except socket.error as e:
                    print(f"{Fore.RED}Connection error: {e}{Fore.RESET}")
                finally:
                    s.close()
                
        except ValueError:
            print(f"{Fore.RED}Invalid command format. Use: connect <PORT> <IP>{Fore.RESET}")
    
        def scan_port(ip, port):
            try:
                sock = socket.socket()
                sock.connect((ip, port))
                print("[+] Port Opened " + str(port))
            except:
                pass
  
        def scan(target, ports):
            print('\n' + ' Starting Scan For'+ str(target)) 
            for port in range(1,ports):
                scan_port(target, port)
    

    elif key == 'exit':
            break
    else:
        print(f"{Fore.RED}Invalid key 'help', 'scantom', 'connect', 'disconnect', 'connlist', 'info', 'exit'. please try again.{Fore.RESET}")

