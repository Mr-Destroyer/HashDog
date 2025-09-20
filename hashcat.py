#HashCat Helping tool thats help you to crack passwords easily 
#developed by mohammad zim
#Github: Mr-Destroyer
#Facebook: Faisal Iqbal (Abdullah)


import os
import time
from colorama import Fore
import sys

#clear the screen
os.system("clear")
##################

def banner():
    print(Fore.CYAN + """
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\        
        \:::\    \               \:::\    \              /::::|   |        
         \:::\    \               \:::\    \            /:::::|   |        
          \:::\    \               \:::\    \          /::::::|   |        
           \:::\    \       Zim     \:::\    \        /:::/|::|   |        
            \:::\    \              /::::\    \      /:::/ |::|   |        
             \:::\    \    ____    /::::::\    \    /:::/  |::|___|______  
              \:::\    \  /\   \  /:::/\:::\    \  /:::/   |::::::::\    \ 
_______________\:::\____\/::\   \/:::/  \:::\____\/:::/    |:::::::::\____\
\::::::::::::::::::/    /\:::\  /:::/    \::/    /\::/    / ~~~~~/:::/    /
 \::::::::::::::::/____/  \:::\/:::/    / \/____/  \/____/      /:::/    / 
  \:::\~~~~\~~~~~~         \::::::/    /                       /:::/    /  
   \:::\    \               \::::/____/                       /:::/    /   
    \:::\    \               \:::\    \       Destroyer      /:::/    /    
     \:::\    \               \:::\    \                    /:::/    /     
      \:::\    \               \:::\    \                  /:::/    /      
       \:::\____\               \:::\____\                /:::/    /       
        \::/    /                \::/    /                \::/    /        
         \/____/                  \/____/                  \/____/         
                                                                    
    """)

def main():
    print(Fore.GREEN + "                {1}MD5 [RAW HASH]                               ")
    print(Fore.GREEN + "                {2}SHA1 [RAW HASH]                              ")
    print(Fore.GREEN + "                {3}MD4 [RAW HASH]                               ")
    print(Fore.GREEN + "                {4}SHA2-224 [RAW HASH]                          ")
    print(Fore.GREEN + "                {5}SHA2-256 [RAW HASH]                          ")
    print(Fore.GREEN + "                {6}SHA2-384 [RAW HASH]                          ")
    print(Fore.GREEN + "                {7}SHA3-512 [RAW HASH]                          ")
    print(Fore.GREEN + "                {8}RIPEMD-160 [RAW HASH]                        ")
    print(Fore.GREEN + "                {9}BLAKE2b-512 [RAW HASH]                       ")
    print(Fore.GREEN + "                {10}Half MD5 [RAW HASH]                         ")
    print(Fore.GREEN + "                {11}SipHash [RAW HASH]                          ")
    print(Fore.GREEN + "                {12}SHA1 with salt [SLAT , PASS]                ")
    print(Fore.GREEN + "                {13}MD5 with salt [SALT , PASS]                 ")
    print(Fore.GREEN + "                {14}MD4 with salt [SALT , PASS]                 ")
    print(Fore.GREEN + "                {15}SHA256 with salt [SALT , PASS]              ")
    print(Fore.GREEN + "                {16}SHA512 with salt [SALT , PASS]              ")
    print(Fore.GREEN + "                {17}Wifi Password {.CAP} [Network protocol]     ")
    print(Fore.GREEN + "                {18}Wifi Password {.HCCAPX} [Network protocol]  ")
    print(Fore.GREEN + "                {19}Wifi Passworf {.HCCAP} [Network protocol]   ")
    print(Fore.GREEN + "                {20}About                                       ")
    print(Fore.GREEN + "                {21}Join Us                                     ")
    print(Fore.GREEN + "                {22}Exit                                        ")



def md5():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 0 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 0 {hasH} {wordlist} --show")

def md4():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 900 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 900 {hasH} {wordlist} --show")

def SHA2(): #it is sha2-224
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 1300 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 1300 {hasH} {wordlist} --show")

def SHA1():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 100 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 100 {hasH} {wordlist} --show")

def SHA256():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 1400 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 1400 {hasH} {wordlist} --show")

def SHA384():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 10800 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 10800 {hasH} {wordlist} --show")

def SHA512():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 17600 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 17600 {hasH} {wordlist} --show")

def RIPEMD():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 6000 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 6000 {hasH} {wordlist} --show")

def BLAKE2b():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 600 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 600 {hasH} {wordlist} --show")

def Half_MD5():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 5100 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 5100 {hasH} {wordlist} --show")

def SipHash():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 10100 {hasH} {wordlist}")
    os.system(f"hashcat -a 0 -m 10100 {hasH} {wordlist} --show")

def MD5_SATL():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    slt = input("[#]salt: ")
    os.system(f"hashcat -a 0 -m 20 {hasH}:{salt} {wordlist}")
    os.system(f"hashcat -a 0 -m 20 {hasH}:{salt} {wordlist} --show")

def SHA1_SALT():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    slt = input("[#]salt: ")
    os.system(f"hashcat -a 0 -m 120 {hasH}:{salt} {wordlist}")
    os.system(f"hashcat -a 0 -m 120 {hasH}:{salt} {wordlist} --show")

def SHA256_SALT():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    slt = input("[#]salt: ")
    os.system(f"hashcat -a 0 -m 1420 {hasH}:{salt} {wordlist}")
    os.system(f"hashcat -a 0 -m 1420 {hasH}:{salt} {wordlist} --show")

def SHA512_SALT():
    os.system("clear")
    hasH = input("[#]Hash: ")
    wordlist = input("[#]wordlist: ")
    slt = input("[#]salt: ")
    os.system(f"hashcat -a 0 -m 1720 {hasH}:{salt} {wordlist}")
    os.system(f"hashcat -a 0 -m 1720 {hasH}:{salt} {wordlist} --show")

def Wifi_Cap():
    os.system("clear")
    file = input("[#]cap file: ")
    wordlist = input("[#]wordlist: ")
    target = input("[#]name of hccapx file: ")
    w_target = "target.hccapx"
    os.system(f"aircrack-ng {file} -j {target}")
    os.system(f"hashcat -a 0 -m 2500 {w_target} {wordlist}")
    os.system(f"hashcat -a 0 -m 2500 {w_target} {wordlist} --show")

def Wifi_hccapx():
    os.system("clear")
    file = input("[#]HCCAPX file: ")
    wordlist = input("[#]wordlist: ")
    os.system(f"hashcat -a 0 -m 2500 {file} {wordlist}")
    os.system(f"hashcat -a 0 -m 2500 {hasH} {wordlist} --show")

def slow(y):
    for x in y+'\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.1)

def About():
    os.system("clear")
    slow("My name is Mohammd Zim and I'm a student and an ethical hacker")
    slow("This tool is made for who have some issue with hashcat \n this tool is for educational purposes only so don't use this tool for any illegal activities \n speciall I add this with wifi hacking , you just need the handshake file that's it , it will crack fater than aircrack-ng")


def Join():
    os.system("coming soon")
    time.sleep(5)
    main()




while True:
    banner()
    main()
    choose = input("[#]choose:~~> ")
    os.system("clear")
    if choose == '1':
        md5()
    elif choose == '2':
        SHA1()
    elif choose == '3':
        MD4()
    elif choose == '4':
        SHA2()
    elif choose == '5':
        SHA256()
    elif choose == '6':
        SHA384()
    elif choose == '7':
        SHA512()
    elif choose == '8':
        RIPEMD()
    elif choose == '9':
        BLAKE2b()
    elif choose == '10':
        Half_MD5()
    elif choose == '11':
        SipHash()
    elif choose == '12':
        SHA1_SALT()
    elif choose == '13':
        MD5_SATL()
    elif choose == '14':
        print("not available")
        main()
    elif choose == '15':
        SHA256_SALT()
    elif choose == '16':
        SHA512_SALT()
    elif choose == '17':
        Wifi_Cap()
    elif choose == '18':
        Wifi_hccapx()
    elif choose == '19':
        print("OLD MEthod will not work!")
        main()
    elif choose == '20':
        About()
    elif choose == '21':
        Join()
    elif choose == '22':
        break
    else:
        print("Wrong Input!")
        time.sleep(5)
        main()
    
        


