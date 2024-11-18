'''
Noah Ham
17 Nov 2024
Ver 1.1

Creates a txt file because TextEdit is dumb and can't do that
'''

import tkinter as tk
from tkinter import filedialog
import subprocess

def main():
    # Creates but hides tkinter window
    root = tk.Tk()
    root.withdraw()

    # Asks where to save file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    # Closes if nothing gets selected
    if not file_path:
        return

    # Creates the text file in the desired directory
    if file_path:
        with open(file_path, "w") as file:
            pass
        subprocess.call(["open", "-a", "TextEdit", file_path]) # Opens the file in TextEdit to actually be used

if __name__ == "__main__":
    main()