import os
import subprocess

import keylogger
import DDOS
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
2.Hash decryption
3.wifi DDOS
""")

# selecting of attack
print("Select the tools: ",end="")
switch =int(input())
if (switch == 1):
  keylogger.klogger()
  

elif(switch == 2):
  import hashcat
  hashcat.hcat()
  

elif(switch==3):
  DDOS.Ds()
  