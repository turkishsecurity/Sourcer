
import os
import time
import urllib.request
print("Lütfen Bekleyin..")
time.sleep(0.2)
os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet XALE ")
print(" ")
site = input("HTML Kodu Çekilecek Site: (Örnek: https://www.google.com/) ")

htm = urllib.request.urlopen(site)
print(htm.read())
