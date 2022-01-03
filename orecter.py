import requests
import threading
from colorama import Fore, Back, Style


print(
        Fore.YELLOW +
         """
   ___     _______                       _                     
 .'   `.  |_   __ \                     / |_                   
/  .-.  \   | |__) |    .---.   .---.  `| |-'  .---.   _ .--.  
| |   | |   |  __ /    / /__\\ / /'`\]  | |   / /__\\ [ `/'`\] 
\  `-'  /  _| |  \ \_  | \__., | \__.   | |,  | \__.,  | |     
 `.___.'  |____| |___|  '.__.' '.___.'  \__/   '.__.' [___]                                    
        

                                
                                          [ twitter.com/r00t_nasser ]
                                          [ Snapchat : aaa.saq ]

        """ + Fore.RESET)
print()
print()
file = open('word.txt','r')
payloads = open('payloads.txt','r')
def Send_req(url,payload):
    while url[-1] != '=':
        url = url[:-1]
    url = url.replace("=",f"={payload}")

    try:

        res = requests.get(url)
        if "we_get_it.__check_back_daily" in res.text:
           print(Fore.GREEN +'Open Redirect Found At   -->','   ' , f"{url}" + Fore.RESET)


    except Exception as e:
        pass
file = file.readlines()
for payload in payloads:
    for url in file:
        url = url.strip('\n')
        payload = payload.strip('\n')
        threading.Thread(target=Send_req,args=(url,payload,)).start()


