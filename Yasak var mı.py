#Made By Dolyetyus

import datetime
from colorama import Fore, Back, init, Style
import sys
import time

init(autoreset="true")

yaş = int(input("Kaç Yaşındasınız: "))
zaman = datetime.datetime.now()
saat = zaman.hour
gün = zaman.weekday()

if(gün>=4 and saat>=21):
    print(Fore.RED+Style.BRIGHT+"Dışarı Çıkman Yasak")
    time.sleep(5)
    sys.exit()

else: 
    if(gün<4 and saat<21 and saat>5):
        iş = input("Çalışıyor musunuz(E/H): ")
        iş=iş.upper()
        if (iş=="E" or iş=="EVET"):
            print(Fore.GREEN+Style.BRIGHT+"Dışarı Çıkabilirsin")
            time.sleep(5)
            sys.exit()
        elif (iş == "H" or iş == "HAYIR"):
            if(yaş > 20 and yaş < 65):
                print(Fore.GREEN+Style.BRIGHT+"Dışarı Çıkabilirsin")
                time.sleep(5)
                sys.exit()
            elif(yaş >= 65 and saat >= 10 and saat < 13):
                print(Fore.GREEN+Style.BRIGHT+"Dışarı Çıkabilirsin")
                time.sleep(5)
                sys.exit()
            elif(yaş <= 20 and saat >= 13 and saat < 16):
                print(Fore.GREEN+Style.BRIGHT+"Dışarı Çıkabilirsin")
                time.sleep(5)
                sys.exit()
        else:
            print(Fore.RED+Style.BRIGHT+"Dışarı Çıkman Yasak")
            time.sleep(5)
            sys.exit()
