import os
from pynput import keyboard
import subprocess
import time

def on_press(key):
    """Listens for save key combo to save the file."""
    try:
        # Normalize key input
        k = key.char.lower() if hasattr(key, 'char') and key.char else key
    except AttributeError:
        k = key

    pressed_keys.add(k)

    if all(k in pressed_keys for k in COMBO):
        time.sleep(0.25)  # Give TextEdit a moment to save
        save_file()
        return False  # Stop listener after action
    return None

def on_release(key):
    """Removes key from pressed keys on release."""
    try:
        k = key.char.lower() if hasattr(key, 'char') and key.char else key
    except AttributeError:
        k = key
    pressed_keys.discard(k)

def create_file():
    """Creates a temporary text file and opens it in TextEdit."""
    file_path = "/tmp/Untitled Text Document.txt"
    open(file_path, "w").close()
    subprocess.call(["open", "-a", "TextEdit", file_path])

def save_file():
    """Saves the file using a native Save As dialog in TextEdit."""
    original_path = "/tmp/Untitled Text Document.txt"

    try:
        # Open a Save As dialog in TextEdit using AppleScript
        script = f'''
        tell application "TextEdit"
            activate
            set docRef to open POSIX file "{original_path}"

            -- Prompt the user with a native Save dialog
            set savePath to POSIX path of (choose file name with prompt "Save your text file as:" default name "Untitled.txt")
            save docRef in POSIX file savePath
            close docRef saving no

            -- Open the newly saved file
            open POSIX file savePath
        end tell

        return savePath
        '''
        subprocess.check_output(["osascript", "-e", script])

        if os.path.exists(original_path):
            os.remove(original_path) # Clean up the temp file

    except subprocess.CalledProcessError:
        print("Save canceled or failed.")

if __name__ == "__main__":
    pressed_keys = set()
    COMBO = {keyboard.Key.cmd, 's'}

    create_file()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
