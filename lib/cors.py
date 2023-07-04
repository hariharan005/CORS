#!/usr/bin/env python3

#Required libraries for this Project
import sys
from requests import get
import os
from colorama import Fore
import getpass


#This variable is used to store the OS username
username = getpass.getuser()

#This function will holds the banner of the project
def banner():
	text = '''
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
	+     CORS-Analyzer 🛠️ is a tool used to indentify cross-origin      +\n
	+     resource sharing vulnerabilities                               +\n
	+     Use this tool at your own risk                                 +\n
	+     Usage might be illegal in certain circumstances                +\n
	+     Designed for educational purposes only                         +\n
	+     Author: @crypto_grapper_                                       +\n
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
	print(Fore.GREEN + text, "\n")
	greeting = Fore.GREEN + "Hi " + Fore.YELLOW + username
	print(greeting + "\n")


def action():
	url = sys.argv[1]
	response = get(url, headers={'User-Agent': 'Mozilla/5.0', 'Origin': 'https://example.com'})
	status = response.headers
	print('\n')
	#print(Fore.WHITE, url)
	#print(Fore.WHITE, status)
	if 'Access-Control-Allow-Origin' and 'Access-Control-Allow-Credentials' in status:
		print(Fore.WHITE + " Vulnerable:  " + url, "\n")
		print(Fore.RED + "   Acess-Control-Allow-Origin header found")
		print(Fore.RED + "   Access-Control-Allow-Credentials header found \n")
		allow_origin = status['Access-Control-Allow-Origin']
		print("   Access-Control-Allow-Origin: ", allow_origin, "\n")
		allow_credentials = status['Access-Control-Allow-Credentials']
		print("   Access-Control-Allow-Credentials:", allow_credentials, "\n")
	else:
		print(Fore.WHITE + " Not Vulnerable: " + url, "\n")
		print(Fore.GREEN + "   Access-Control-Allow-Origin header not found")
		print(Fore.GREEN + "   Access-Control-Allow-Credentials header not found")
	"""print("Response Headers:")
	for header, value in status.items():
		print(header + ": " + value)"""

def help():
	print(Fore.WHITE)
	banner()
	print(Fore.GREEN + "USAGE: \n")
	print(Fore.WHITE + "For scanning:  cat <domain.txt> | xargs -n1 -P10 python3 cors.py \n")
	print(Fore.WHITE + "For scanning with output:  cat <domain.txt> | xargs -n1 -P10 python3 corss.py | tee -a <output.txt> \n")
	
if (len(sys.argv)<=1):
	os.system("clear")
	banner()
	print(Fore.WHITE)
	print("You must provide a target. Use -h or --help for help. \n")
	print("Usage: python3 cors.py -h or  python3 cors.py --help \n")

	print(" ")
	sys.exit()        

elif (str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
	os.system("clear")
	help()
	sys.exit()
	
elif (len(sys.argv)>=1):
	os.system("clear")
	banner()
	action()
