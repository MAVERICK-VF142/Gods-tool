import subprocess
import os

def display_hashcat_logo():
    print("""
    ██╗░░██╗░█████╗░░██████╗██╗░░██╗  ██████╗░███████╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗
    ██║░░██║██╔══██╗██╔════╝██║░░██║  ██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
    ███████║███████║╚█████╗░███████║  ██║░░██║█████╗░░██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║
    ██╔══██║██╔══██║░╚═══██╗██╔══██║  ██║░░██║██╔══╝░░██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║
    ██║░░██║██║░░██║██████╔╝██║░░██║  ██████╔╝███████╗╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░╚═╝░░░╚═╝╚════╝░╚═╝░░╚══╝
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
    """)

def prompt_for_file(message):
    while True:
        file_path = input(message)
        if os.path.isfile(file_path):
            return file_path
        else:
            print("Invalid file path. Please try again.")

def prompt_for_integer(message, options):
    while True:
        try:
            print(options)
            value = int(input(message))
            if value in options:
                return value
            else:
                print("Invalid input. Please enter a valid option.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def prompt_for_rule():
    print("Select the rule:")
    print("1) No rules")
    print("2) Best64")
    print("3) Combinator")
    print("4) Generator")
    while True:
        rule_choice = input("Enter your choice: ")
        if rule_choice in ("1", "2", "3", "4"):
            return rule_choice
        else:
            print("Invalid choice. Please select a valid rule.")

def prompt_for_wordlist():
    print("Select an option for the wordlist:")
    print("1) Use default Kali Linux wordlist (rockyou.txt)")
    print("2) Enter a custom wordlist path")
    while True:
        option = input("Enter your choice: ")
        if option == "1":
            return "/usr/share/wordlists/rockyou.txt"
        elif option == "2":
            return prompt_for_file("Enter the path to the wordlist file: ")
        else:
            print("Invalid choice. Please select a valid option.")

def run_hashcat(hashcat_path, hash_file, hash_type, attack_mode, wordlist, rule):
    args = [hashcat_path, "-a", str(attack_mode), "-m", str(hash_type), hash_file, wordlist]
    if rule == "2":
        args.append("--rules=/usr/share/hashcat/rules/best64.rule")
    elif rule == "3":
        args.append("--rules=/usr/share/hashcat/rules/combinator.rule")
    elif rule == "4":
        args.append("--rules=/usr/share/hashcat/rules/generated.rule")

    process = subprocess.run(args, text=True, capture_output=True)

    # Combine stdout and stderr into a single output variable
    output = process.stdout + process.stderr

    if process.returncode == 0:
        return output
    else:
        return output


def main():
    display_hashcat_logo()

    hashcat_path = "/usr/bin/hashcat"  # Change this path if necessary
    hash_file = prompt_for_file("Enter the path to the hash file: ")

    hash_types = [0, 1000, 1400]  # Add more hash types if needed
    hash_type = prompt_for_integer("0-MD5 \n1000-NTLM \n1400-SHA256\n Enter the hash type: ", hash_types)

    attack_modes = [0, 3, 6]  # Add more attack modes if needed
    attack_mode = prompt_for_integer("0-Straight\n3-Mask\n6-Combinator\nEnter the attack mode: ", attack_modes)

    rule_choice = prompt_for_rule()
    wordlist = prompt_for_wordlist()

    output = run_hashcat(hashcat_path, hash_file, hash_type, attack_mode, wordlist, rule_choice)

    # Print the output on the terminal
    print("Hashcat Output:")
    print(output)

    # Write the output to a text file
    with open("hashcat_output.txt", "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()
