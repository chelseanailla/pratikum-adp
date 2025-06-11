import time
import os
from termcolor import colored
import cowsay

teks = "HAPPY EID ALL!!!      "  
lebar = 20  
durasi = 20  
jeda = 0.2  

steps = int(durasi / jeda)

for i in range(steps):
    mulai = i % len(teks)
    scrolled = (teks + teks)[mulai:mulai+lebar]
    os.system('cls' )
    sapi = cowsay.cow(colored(scrolled, 'green'))   
    print(sapi)
    time.sleep(jeda)