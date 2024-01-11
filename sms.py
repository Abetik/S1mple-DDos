"""

Author:Gheris :)

"""
#!/usr/bin/python3
from pystyle import Colors, Colorate, Write #pip install pystyle
import requests # pip install requests
import os
from colorama import init, Fore # pip install colorama


os.system('cls' if os.name == 'nt' else 'clear')

# colors
init()
GREEN = Fore.GREEN
RED = Fore.RED

print(f"{RED} WARNING : {GREEN}Dont use this to harm others ! This script is only for and educational purposes not to prank")
Write.Print("""
 __  _                 _           ___   ___  ___  __    
/ _\/ |_ __ ___  _ __ | | ___     /   \ /   \/___\/ _\   
\ \ | | '_ ` _ \| '_ \| |/ _ \   / /\ // /\ //  //\ \    
_\ \| | | | | | | |_) | |  __/  / /_/// /_// \_// _\ \   
\__/|_|_| |_| |_| .__/|_|\___| /___,'/___,'\___/  \__/   
                |_|                                     
\n""",Colors.blue_to_red, interval=0.01)



def main():
    phone = Write.Input("[*] Enter number of the victim : ",Colors.yellow_to_red)
    print(f">>> {phone}")
    message = Write.Input("[*] ENTER YOUR MSG :",Colors.blue_to_white)
    print(f">>> {message}")
    resp = requests.post('https://textbelt.com/text', {
    'phone': f'{phone}',
    'message': f'{message}',
    'key': 'textbelt',
    })
    print("\n")
    print(f"{GREEN} {resp.json()}")


if __name__ == "__main__":
    main()
