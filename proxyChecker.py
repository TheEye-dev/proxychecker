import random
import requests
from time import sleep
from colorama import Fore

# IF YOU HAVE ERROR WITH THIS FOLLOW THE STEP's :
# 1- OPEN " CMD " BY CLICKING ON " WINDOWS + R "
# 2- WRITE INSIDE THE " CMD or TERMINAL " pip3 install [name of module you dont have]
# 3- IF YOU HAVE ANY PROBLEM CONTACT WITH ME AT MY INSTAGRAM : @iamlindos

                            ## ENJOY MY PROXY CHECKER TOOL *^* ##


### Random File Name Generator ###

global letter_number
global file_random_name
letter_number = "abcdefghijklmnopqrstuvwxyz1234567890"
file_random_name = "".join(random.sample(letter_number, 4))

### Intro & Outro Design ###

print(Fore.RED + '''

MMP""MM""YMM `7MM               `7MM"""YMM                  
P'   MM   `7   MM                 MM    `7                  
     MM        MMpMMMb.  .gP"Ya   MM   d `7M'   `MF'.gP"Ya  
     MM        MM    MM ,M'   Yb  MMmmMM   VA   ,V ,M'   Yb 
     MM        MM    MM 8M""""""  MM   Y  , VA ,V  8M"""""" 
     MM        MM    MM YM.    ,  MM     ,M  VVV   YM.    , 
   .JMML.    .JMML  JMML.`Mbmmd'.JMMmmmmMMM  ,V     `Mbmmd' 
                                            ,V              
                                         OOb"

                    +-----------------+
                    |  Proxy Checker  |
                +---+-----------------+---+
                | [#] insta : @ IamLindos |
                +-------------------------+

''')

def coded() :
    print(Fore.LIGHTWHITE_EX + "\n --------------# Coded By : @ IamLindos - TheEye #-------------- ")
    print(Fore.LIGHTBLACK_EX + "          --------# Thanks For Using This Tool #-------- ")
    print(Fore.LIGHTRED_EX + "                   -------# Made With Love #------- \n")

### User Input ###

print(Fore.LIGHTBLACK_EX + "=" * 20)
proxylist = input("Enter The Proxy File : ")

### Proxy Scanning Code & Result ###

file = proxylist
the_list = open(file, "r")

for proxy in the_list :
    try :
        scan = requests.get("https://ipinfo.io/" + proxy)
        if ('"message": "Please provide a valid IP address"') in scan.text :
            sleep(0.3)
            print(Fore.RED + "[!] {} : OFFLINE".format(proxy))

        else :
            file = open(file_random_name + "_availableProxy.txt", "a")
            file.write(proxy)
            file.close()
            sleep(0.3)
            print(Fore.GREEN + "[+] {} : ONLINE".format(proxy))

    except :
        print(Fore.YELLOW + "[?] Warning: Error")
        coded()
    
print(Fore.BLUE + "All ONLINE Proxy's Have Been Saved In {}".format(file_random_name + "_availableProxy.txt"))
coded()