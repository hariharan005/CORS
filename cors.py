from requests import get

cyan ='\033[36m'
yellow ='\033[33m'
white = '\033[37m'

path = input("Enter the file path: ")
print("")
try:
     with open(path) as f:
            list = f.readlines()
     list = [x.strip() for x in list]

     for url in list:
             #payload = headers={'User-Agent': 'Mozilla/5.0', 'Origin': 'https://google.com'}
             response = get(url, headers={'User-Agent': 'Mozilla/5.0', 'Origin': 'https://example.com'})
             status = response.headers
             print("\n\n")
             print(cyan, url)
             print("\n")
             print(white, status)
             print("")
except:
       print("Error")
