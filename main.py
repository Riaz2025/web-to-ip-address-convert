from sys import modules

import modiul
import socket
import pyfiglet
from termcolor import colored

banner=colored(pyfiglet.figlet_format("WEB TO IP ADDRESS"), "Green")
print(banner)
domain_name = input("domain_name_input ")
ip = socket.gethostbyname(domain_name)
print(ip)