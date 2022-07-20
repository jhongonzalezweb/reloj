
import os
import datetime
from time import sleep
from datetime import datetime

os.system("clear")
print("Afuera")
while True:
    file = open("index.html", "w")
    #Fecha actual
    nowC = datetime.now()
    now = str(nowC)
    now3  = now[11:-10]
    #print(now)
    ref = 60
    HTML = '<!DOCTYPE html><html lang="en"><head><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta http-equiv="refresh" content="{}" ><title>Reloj Relojito</title></head><body><h1 style="margin: 0px; padding: 0px; background: black; color:gold; text-align: center; height: 100vh; font-size: 450px;">{}</h1></body></html>'.format(ref,now3)
    file.write(HTML)
    file.close()
    sleep(ref)
    print("Pasaron {}".format(ref))