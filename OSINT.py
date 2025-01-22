import requests
import sys
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

print(rf"""
{Fore.YELLOW}
    Coded By GhosT LulzSec
    Telegram : @WW6WW6WW6
    GitHub: https://github.com/69d9
    All rights reserved.

            o  o   o  o
         |\/ \^/ \/|  
         |,-------.|  
       ,-.(|)   (|),-. 
       \_*._ ' '_.* _/  
        /-.--' .-`\  
   ,--./    `---'    \,--. 
   \   |(  )     (  )|   /  
hjw \  |         |  /  
`97  \ | /|\     /|\ | /  
     /  \-._     _,-/  \  
    //| \  `---'  // |\\  
   /,-.,-.\       /,-.,-.\  
  o   o   o      o   o    o  
""")

shape = f"{Fore.BLUE}[{Fore.RED}+{Fore.BLUE}]"

print(f"{shape} {Fore.RED}My channel: {Fore.GREEN}https://t.me/HereMalaria")
print(f"{shape} {Fore.RED}My Telegram: {Fore.GREEN}ww6ww6ww6\n")

if len(sys.argv) != 2:
    print(f"{Fore.RED}Usage: python {sys.argv[0]} <IP or Domain>")
    sys.exit(1)

ip = sys.argv[1]

url = f"http://ip-api.com/json/{ip}"
response = requests.get(url)

data = response.json()

if data["status"] == "success":
    latitude = data["lat"]
    longitude = data["lon"]
    city = data["city"]
    country = data["country"]
    isp = data["isp"]
    status = data["status"]
    timezone = data["timezone"]
    AS = data["as"]
    org = data["org"]
    
    print(f"{shape} {Fore.RED}Status: {Fore.GREEN}{status}")
    print(f"{shape} {Fore.RED}ISP: {Fore.GREEN}{isp} {Fore.RED}AS: {Fore.GREEN}{AS}")
    print(f"{shape} {Fore.RED}Organization: {Fore.GREEN}{org}")
    print(f"{shape} {Fore.RED}Location: {Fore.GREEN}{city}, {country}")
    print(f"{shape} {Fore.RED}Timezone: {Fore.GREEN}{timezone}")
    print(f"{shape} {Fore.RED}Latitude: {Fore.GREEN}{latitude}, {Fore.RED}Longitude: {Fore.GREEN}{longitude}")
else:
    status = data["status"]
    print(f"{Fore.RED}Status: {Fore.GREEN}{status}")
    print(f"{Fore.RED}Invalid IPv4 address or geolocation not available!")
    print(f"{Fore.YELLOW}Try entering (ip)/24 or ensure no spaces.")
