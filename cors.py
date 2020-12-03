import sys
from requests import get
import os

cyan ='\033[36m'
yellow ='\033[33m'
white = '\033[37m'
def banner():
	print (yellow)
	print (" .-----------------------------.           ")
	print (" |  Hi Hackers                 |           ")
	print (" |  Tool   : "+ cyan + "C0RS              "+yellow+     "|")
	print (" |  Author : @crypto_grapper_  |           ")
	print (" |           Jai Hind          |           ")
	print (" '-----------------------------'           ")
	print ("                 ^      (\_/)    ")
	print ("                 '----- (O.o)    ")
	print ("                        (> <)    ")
	print (" ")
def action():
	url = sys.argv[1]
	response = get(url, headers={'User-Agent': 'Mozilla/5.0', 'Origin': 'https://example.com'})
	status = response.headers
	print("\n\n")
	print(cyan, url)
	print("\n")
	print(white, status)
	print("")

def help():
	banner()
	print(cyan + "USAGE: \n")
	print(yellow + "For scanning:  cat <domain.txt> | xargs -n1 -P10 python3 corss.py \n")
	print(yellow + "For scanning with output:  cat <domain.txt> | xargs -n1 -P10 python3 corss.py | tee -a <output.txt>")
	
if (len(sys.argv)<=1):
	os.system("clear")
	banner()
	print("You must provide a target. Use -h or --help for help. \n")
	print("EG: python3 cors.py -h or  python3 cors.py --help")
	print(" ")
	sys.exit()        

elif (str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
	os.system("clear")
	help()
	sys.exit()
	
elif (len(sys.argv)>=1):
	action()
