import sys
from requests import get

cyan ='\033[36m'
yellow ='\033[33m'
white = '\033[37m'

def action():
        url = sys.argv[1]
        response = get(url, headers={'User-Agent': 'Mozilla/5.0', 'Origin': 'ht>
        status = response.headers
        print("\n\n")
        print(cyan, url)
        print("\n")
        print(white, status)
        print("")

action()


