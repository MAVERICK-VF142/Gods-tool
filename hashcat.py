def hcat():
    
    print("""
    
██╗░░██╗░█████╗░░██████╗██╗░░██╗  ██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗██╔════╝██║░░██║  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
███████║███████║╚█████╗░███████║  ██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║
██╔══██║██╔══██║░╚═══██╗██╔══██║  ██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║
██║░░██║██║░░██║██████╔╝██║░░██║  ██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
    """)

import subprocess

# Set the path to the Hashcat executable
hashcat_path = "/usr/bin/hashcat"

# Prompt the user for the path to the hash file
hash_file = input("Enter the path to the hash file: ")

# Prompt the user for the hash type
hash_type = input("Enter the hash type (e.g., 0 for MD5, 1000 for NTLM): ")

# Prompt the user for the attack mode
attack_mode = input("Enter the attack mode (e.g., 0 for straight, 3 for mask): ")

# Prompt the user to select the rule
print("Select the rule:")
print("1) No rules")
print("2) Best64")
print("3) Combinator")
print("4) generator")
rule_choice = input("Enter your choice: ")

if rule_choice == "1":
    rule = ""
elif rule_choice == "2":
    rule = "/usr/share/hashcat/rules/best64.rule"
elif rule_choice == "3":
    rule = "/usr/share/hashcat/rules/combinator.rule"
elif rule_choice == "4":
    rule = "/usr/share/hashcat/rules/generated.rule"
else:
    print("Invalid choice.")
    exit()

# Set the path to the wordlist
wordlist = input("Enter the path to the hash file:" )

# Set the command-line arguments for Hashcat
args = [hashcat_path,  "-a", attack_mode, "-m", hash_type, hash_file, wordlist, rule ,"--show"]

# Run the Hashcat command and capture the output
process = subprocess.run(args, capture_output=True)

# Print the output and error messages (if any)
print(process.stdout.decode())
print(process.stderr.decode())
