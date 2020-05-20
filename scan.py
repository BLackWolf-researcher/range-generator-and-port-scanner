import sys
import time
import socket
import threading
from colorama import *

init(convert=True)

green = Fore.GREEN
reset = Fore.RESET
red = Fore.RED
yellow = Fore.YELLOW

f = open("SSH-LIST.txt", 'w')

def try_host(host, port):
    try:
      s = socket.socket(socket.AF_INET)
      s.connect((host,port))
      print("open --> " + green +  host + reset)
      f.write(host + "\n")
      print(host + " --> " + yellow + "added to list" + reset)
      s.close()
    except socket.timeout:
      print(host + "--- === timeout exeded! ===] ---")
    except:
      print(host + " <-- " + red + "closed!" + reset)


for x in range(0, 999):
    try:
      ran = sys.argv[1]
    except:
      print("usage: python scan.py  <ip range/ 192.168.0. > --> iplist saved in SSH-LIST.txt ")
      sys.exit()
    host = ran + str(x)
    
    t = threading.Thread(target=try_host, args=(host, 22)).start()
    time.sleep(0.2)

f.close()
