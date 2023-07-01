#!/usr/bin/env python3


#Required libraries for this Project
import sys
from requests import get
import os
from colorama import Fore


#This function will holds the banner of the project
def banner():
	text = '''
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
	+     CORS-Finder 🛠️ is a tool used to indentify cross-origin        +\n
	+     resource sharing vulnerabilities                               +\n
	+     Use this tool at your own risk                                 +\n
	+     Usage might be illegal in certain circumstances                +\n
	+     Designed for educational purposes only                         +\n
	+     Author: @crypto_grapper_                                       +\n
	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
	print(Fore.GREEN + text, "\n")


def action():
	url = sys.argv[1]
	response = get(url, headers={'User-Agent': 'Mozilla/5.0', 'Origin': 'https://example.com'})
	status = response.headers
	print("\n")
	print(Fore.GREEN, url)
	print("\n")
	print(Fore.WHITE, status)
	print("")

def help():
	print(Fore.WHITE)
	banner()
	print(Fore.GREEN + "USAGE: \n")
	print(Fore.YELLOW + "For scanning:  cat <domain.txt> | xargs -n1 -P10 python3 cors.py \n")
	print(Fore.YELLOW + "For scanning with output:  cat <domain.txt> | xargs -n1 -P10 python3 corss.py | tee -a <output.txt> \n")
	
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
	action()
